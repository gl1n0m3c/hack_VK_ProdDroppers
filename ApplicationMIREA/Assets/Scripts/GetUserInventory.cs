using Newtonsoft.Json;
using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using System.Net;
using UnityEngine;

public class GetUserInventory : MonoBehaviour
{
    async public void GetInventory()
    {
        using HttpClient httpClient = new();
        int vkId = PlayerPrefs.GetInt(WebUtils.VKIdKey);
        int roomId = WebUtils.CURRENT_ROOM_ID;
        if (roomId == -1)
        {
            OnError(new ArgumentNullException("Room id is not defined"));
            return;
        }
        try
        {
            HttpResponseMessage response = await httpClient.GetAsync(WebUtils.BaseURL + "/rooms/invent/" + vkId + "/" + roomId + "/");
            if (response.IsSuccessStatusCode)
            {
                using HttpContent content = response.Content;
                string json = await content.ReadAsStringAsync();
                GetInventoryResponse responseBody = JsonConvert.DeserializeObject<GetInventoryResponse>(json);
                string[] inventoryStr = responseBody.invent.Split('/');
                int[] inventory = inventoryStr.Select(s =>
                {
                    int result;
                    return int.TryParse(s, out result) ? result : 0; 
                }).ToArray();

                OnSuccess(inventory);
            }
            else
            {
                OnError(new WebException("Something went wrong"));
            }

        }
        catch (Exception e)
        {
            OnError(e);
        }

    }

    private void OnSuccess(int[] rooms)
    {
        foreach (int roomId in rooms)
        {
            Debug.Log(roomId);
        }
    }

    private void OnError(Exception e)
    {
        Debug.Log(e.Message);
    }

}

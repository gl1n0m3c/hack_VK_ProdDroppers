using Newtonsoft.Json;
using System.Linq;
using System.Net.Http;
using System.Net;
using System.Text;
using System;
using UnityEngine;
using TMPro;

public class AttachUserToRoom : MonoBehaviour
{

    [SerializeField]
    public TMP_Text _roomIdText;

    async public void AttachUser()
    {
        /*
         заимплементить логику получения id комнаты
        int roomId = Convert.ToInt32(_roomIdText.text);
        */
        int roomId = 1;

        int vkId = PlayerPrefs.GetInt(WebUtils.VKIdKey);

        using HttpClient httpClient = new();
        try
        {
            using StringContent jsonContent = new(
            JsonConvert.SerializeObject(new
            {
                id_vk = vkId,
                room_id = roomId
            }),
            Encoding.UTF8,
            "application/json");
            HttpResponseMessage response = await httpClient.PostAsync(WebUtils.BaseURL + "rooms/user_to_room/", jsonContent);
            string responseBody = await response.Content.ReadAsStringAsync();
            BaseResponse baseResponse = JsonConvert.DeserializeObject<BaseResponse>(responseBody);
            if (baseResponse.success)
            {
                WebUtils.CURRENT_ROOM_ID = roomId;
                OnSuccess();
            }
            else
            {
                OnError(new WebException(string.Join(" ", baseResponse.description)));
            }

        }
        catch (Exception e)
        {
            OnError(e);
        }
    }

    private void OnSuccess()
    {

    }

    private void OnError(Exception e)
    {
        Debug.Log(e.Message);
    }

}

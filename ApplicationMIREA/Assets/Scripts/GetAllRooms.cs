using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Http;
using UnityEngine;

public class GetAllRooms : MonoBehaviour
{

    private static int _page = 0;

    /*
     * ���� isPagingEnabled ������ ���������: ���� �������� true,
     * �� ������ ����������� ������ ��������, ���� false, 
     * �� ��� ������ �������� ��������� �������� 
     * ��������� ���� _page �������������
     */
    public bool isPagingEnabled = false;

    async public void GetRooms()
    {
        using HttpClient httpClient = new();
        if (!isPagingEnabled)
        {
            _page = 0;
        }
        try
        {
            HttpResponseMessage response = await httpClient.GetAsync(WebUtils.BaseURL + "rooms/list/" + "?page=" + _page);
            if (response.IsSuccessStatusCode)
            {
                using HttpContent content = response.Content;
                string json = await content.ReadAsStringAsync();
                GetAllRoomsResponse responseBody = JsonConvert.DeserializeObject<GetAllRoomsResponse>(json);
                _page++;
                OnSuccess(responseBody.rooms);
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

    private void OnSuccess(List<Room> rooms)
    {
        foreach (Room room in rooms) 
        {
            Debug.Log(room.name);
        }
    }
    
    private void OnError(Exception e)
    {
        Debug.Log(e.Message);
    }

}

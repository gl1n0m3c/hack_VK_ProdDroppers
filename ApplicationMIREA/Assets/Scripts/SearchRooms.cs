using Newtonsoft.Json;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using System.Net;
using UnityEngine;
using TMPro;

public class SearchRooms : MonoBehaviour
{

    private static int _page = 0;

    /*
     * поле isPagingEnabled задает пагинацию: если значение true,
     * то всегда загружается первая страница, если false, 
     * то при каждой успешной прогрузки страницы 
     * приватное поле _page инкрементится
     */
    public bool isPagingEnabled = false;

    /*
     Поменять класс объекта на нужный
    */
    [SerializeField]
    public TMP_Text SearchInputField;


    async public void GetRooms()
    {
        using HttpClient httpClient = new();
        if (!isPagingEnabled)
        {
            _page = 0;
        }
        try
        {
            string query = SearchInputField.text; 
            HttpResponseMessage response = await httpClient.GetAsync(WebUtils.BaseURL + "rooms/list/" + "?page=" + _page + "&" + "start=" + query);
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

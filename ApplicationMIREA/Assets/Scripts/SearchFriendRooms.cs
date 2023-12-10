using Newtonsoft.Json;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using System.Net;
using UnityEngine;
using TMPro;

public class SearchFriendRooms : MonoBehaviour
{

    /*
     * ���� isPagingEnabled ������ ���������: ���� �������� true,
     * �� ������ ����������� ������ ��������, ���� false, 
     * �� ��� ������ �������� ��������� �������� 
     * ��������� ���� _page �������������
     */
    public bool isPagingEnabled = false;

    private static int _page = 0;

    /*
     �������� ����� ������� �� ������
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
            int vkId = PlayerPrefs.GetInt(WebUtils.VKIdKey);
            HttpResponseMessage response = await httpClient.GetAsync(WebUtils.BaseURL + "rooms/friend_room/" + vkId + "/?page=" + _page + "&" + "start=" + query);
            if (response.IsSuccessStatusCode)
            {
                using HttpContent content = response.Content;
                string json = await content.ReadAsStringAsync();
                GetFriendRoomResponse responseBody = JsonConvert.DeserializeObject<GetFriendRoomResponse>(json);
                _page++;
                OnSuccess(responseBody.friends);
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

    private void OnSuccess(List<FriendRoom> rooms)
    {

    }

    private void OnError(Exception e)
    {
        Debug.Log(e.Message);
    }
}

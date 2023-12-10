using Newtonsoft.Json;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using System.Net;
using UnityEngine;

public class GetWaiters : MonoBehaviour
{
    /*
     * поле isPagingEnabled задает пагинацию: если значение true,
     * то всегда загружается первая страница, если false, 
     * то при каждой успешной прогрузки страницы 
     * приватное поле _page инкрементится
     */
    public bool isPagingEnabled = false;

    private static int _page = 0;

    async public void FetchWaiters()
    {
        using HttpClient httpClient = new();
        int vkId = PlayerPrefs.GetInt(WebUtils.VKIdKey);
        if (!isPagingEnabled)
        {
            _page = 0;
        }
        try
        {
            HttpResponseMessage response = await httpClient.GetAsync(WebUtils.BaseURL + "users/waiters/" + vkId + "/?page=" + _page);
            if (response.IsSuccessStatusCode)
            {
                using HttpContent content = response.Content;
                string json = await content.ReadAsStringAsync();
                GetFriendsResponse responseBody = JsonConvert.DeserializeObject<GetFriendsResponse>(json);
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

    private void OnSuccess(List<Friend> friends)
    {
        foreach (Friend friend in friends)
        {
            Debug.Log(friend.id);
        }
    }

    private void OnError(Exception e)
    {
        Debug.Log(e.Message);
    }

}

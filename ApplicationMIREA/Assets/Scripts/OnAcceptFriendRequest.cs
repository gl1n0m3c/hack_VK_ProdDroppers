using Newtonsoft.Json;
using System.Net.Http;
using System.Net;
using System.Text;
using System;
using TMPro;
using UnityEngine;

public class OnAcceptFriendRequest : MonoBehaviour
{

    [SerializeField]
    public TMP_Text _recipientUser;

    async public void OnClick()
    {
        int vkId = PlayerPrefs.GetInt(WebUtils.VKIdKey);

        using HttpClient httpClient = new();
        try
        {
            using StringContent jsonContent = new(
            JsonConvert.SerializeObject(new
            {
                id1_vk = Convert.ToInt32(_recipientUser.text),
                id2_vk = vkId,
            }),
            Encoding.UTF8,
            "application/json");
            HttpResponseMessage response = await httpClient.PostAsync(WebUtils.BaseURL + "friends/accept/", jsonContent);
            string responseBody = await response.Content.ReadAsStringAsync();
            BaseResponse baseResponse = JsonConvert.DeserializeObject<BaseResponse>(responseBody);
            if (baseResponse.success)
            {
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

using Assets.SimpleVKSignIn.Scripts;
using System;
using System.Net.Http;
using UnityEngine;
using Newtonsoft.Json;
using System.Text;

public class OnSignIn : MonoBehaviour
{

    public void OnClick()
    {
        VKAuth.OnTokenResponse += OnTokenResponse;
        VKAuth.SignIn(SignIn);
    }

    private void SignIn(bool success, string error, UserInfo userInfo)
    {
        if (success)
        {
            PostUserData(userInfo);
            OnSuccess(userInfo);
        } 
        else
        {
            OnError(error);
        }
    }

    private static void OnTokenResponse(TokenResponse response)
    {
        int id = Convert.ToInt32(response.user_id);
        Debug.Log($"Access token: {response.access_token}\nVKId: {id}");
        SaveUserData(id, response.access_token);
    }

    private static void SaveUserData(int vkId, string token)
    {
        PlayerPrefs.SetString(WebUtils.AccessTokenKey, token);
        PlayerPrefs.SetInt(WebUtils.VKIdKey, vkId);
    }

    async private static void PostUserData(UserInfo userInfo) 
    {
        string token = PlayerPrefs.GetString(WebUtils.AccessTokenKey);

        using HttpClient httpClient = new();

        try
        {
            using StringContent jsonContent = new(
            JsonConvert.SerializeObject(new
            {
                id_vk = userInfo.id,
                firstname = userInfo.first_name,
                lastname = userInfo.last_name
            }),
            Encoding.UTF8,
            "application/json");
            HttpResponseMessage response = await httpClient.PostAsync(WebUtils.BaseURL + "users/auth/", jsonContent);
            string responseBody = await response.Content.ReadAsStringAsync();
            BaseResponse baseResponse = JsonConvert.DeserializeObject<BaseResponse>(responseBody);
            if (!baseResponse.success)
            {
                OnError(string.Join(" ", baseResponse.description));
            }

        }
        catch (Exception e)
        {
            OnError(e.Message);
        }
    }

    private static void OnSuccess(UserInfo userInfo)
    {

    }

    private static void OnError(string error)
    {
        Debug.Log(error);
    }

}

using System;
using System.Net.Http;
using System.Net;
using UnityEngine;
using Newtonsoft.Json;
using System.Text;
using TMPro;
using System.Linq;

public class OnCreateRoom : MonoBehaviour
{

    [SerializeField] 
    public TMP_Text _roomNameText, _roomPasswordField;

    async public void OnClick()
    {
        string roomName = _roomNameText.text;
        string roomPassword = _roomPasswordField.text;
        int vkId = PlayerPrefs.GetInt(WebUtils.VKIdKey);

        if (roomName.Length == 0 || roomName.Length > 50)
        {
            OnError(WebUtils.WRONG_NAME_LENGTH);
            return;
        }
        else if ((roomPassword.Length != 0 && roomPassword.Length != 6) || !roomPassword.All(c => char.IsDigit(c)))
        {
            OnError(WebUtils.WRONG_PASSWORD);
            return;
        }

        using HttpClient httpClient = new();
        try
        {
            int? intPassword = (roomPassword.Length == 0) ? null : Convert.ToInt32(roomPassword);
            using StringContent jsonContent = new(
            JsonConvert.SerializeObject(new
            {
                id_vk = vkId,
                name = roomName,
                password = intPassword
            }),
            Encoding.UTF8,
            "application/json");
            HttpResponseMessage response = await httpClient.PostAsync(WebUtils.BaseURL + "rooms/create_room/", jsonContent);
            string responseBody = await response.Content.ReadAsStringAsync();
            CreateRoomResponse createRoomResponse = JsonConvert.DeserializeObject<CreateRoomResponse>(responseBody);
            if (createRoomResponse.success)
            {
                int roomId = createRoomResponse.id;
                WebUtils.CURRENT_ROOM_ID = roomId;
                OnSuccess(roomId);
            }
            else
            {
                OnError(createRoomResponse.description.FirstOrDefault());
            }

        }
        catch (Exception e)
        {
            OnError(e.Message);
        }
    }

    private void OnSuccess(int roomId)
    {

    }

    private void OnError(string e)
    {
        switch(e)
        {
            case WebUtils.WRONG_NAME_LENGTH:
                Debug.Log("Wrong RoomName Length");
                break;
            
            case WebUtils.WRONG_PASSWORD:
                Debug.Log("Wrong Password");
                break;
           
            default: 
                Debug.Log(e);
                break;
        }
    }

}

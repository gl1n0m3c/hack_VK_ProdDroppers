using Assets.SimpleVKSignIn.Scripts;
using UnityEngine;

public class OnLogout : MonoBehaviour
{

    public void OnClick()
    {
        VKAuth.SignOut();
    }

}
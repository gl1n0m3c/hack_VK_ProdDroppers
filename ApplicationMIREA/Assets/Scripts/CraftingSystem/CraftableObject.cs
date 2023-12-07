using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

public class CraftableObject : MonoBehaviour
{
    [SerializeField] private int objectID;
    [SerializeField] private string objectName;
    public int GetID()
    {
        return objectID;
    }

    public string GetName()
    {
        return objectName;
    }
}

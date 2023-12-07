using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using Unity.VisualScripting;
using UnityEngine;

public class CraftingTableController : MonoBehaviour
{
    [SerializeField] private LevelController levelController;
    [SerializeField, Tooltip("X stands for first component's ID \n Y xtands for second component's ID \n Z stands for result craftableObject ID")] private List<Vector3Int> recipesList = new();
    [SerializeField] private Transform craftingZoneTransform;
    private Collider craftingZone;
    private List<CraftableObject> objectsOnTable = new();
    private int duplicationId => levelController.DuplicationID;
    private int anyId => levelController.AnyID;
    private IReadOnlyList<GameObject> objectsPrefabsList => levelController.PrefabsList;
    // Start is called before the first frame update
    private void Awake()
    {
        craftingZone = craftingZoneTransform.GetComponent<Collider>();
    }
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
                
    }


    private void OnTriggerEnter(Collider other)
    {
        CraftableObject craftableObject;
        if (other.TryGetComponent<CraftableObject>(out craftableObject))
        {
            objectsOnTable.Add(craftableObject);
            Debug.Log(craftableObject.GetName());
            if(objectsOnTable.Count>=2)
            {
                GameObject newObject, componentA = objectsOnTable[0].gameObject, componentB = objectsOnTable[1].gameObject;
                if (TryCraft(objectsOnTable[0], objectsOnTable[1], out newObject))
                {
                    if (newObject != null)
                    {
                        GameObject.Instantiate(newObject, gameObject.transform.position + Vector3.up, Quaternion.identity);
                        objectsOnTable.Remove(componentA.GetComponent<CraftableObject>());
                        objectsOnTable.Remove(componentB.GetComponent<CraftableObject>());
                        Destroy(componentA);
                        Destroy(componentB);

                    }
                }
            }
        }
        
    }

    private void OnTriggerExit(Collider other)
    {
        CraftableObject craftableObject;
        if (other.TryGetComponent<CraftableObject>(out craftableObject))
        {
            objectsOnTable.Remove(craftableObject);
        }
    }

    public bool TryCraft(CraftableObject componentA, CraftableObject componentB, out GameObject componentResult)
    {
        componentResult = null;
        foreach(var vector in recipesList)
        {
            if ((vector.x == componentA.GetID() && vector.y == componentB.GetID()) || (vector.x == componentB.GetID() && vector.y == componentA.GetID())||((vector.x==componentA.GetID()&&vector.y==anyId)|| (vector.x == componentB.GetID() && vector.y == anyId)))
            {
                if (vector.z != duplicationId)
                {
                    componentResult = objectsPrefabsList[vector.z];
                    return true;
                }
                else
                {
                    if(componentA.GetID() == vector.y)
                    {
                        componentResult = objectsPrefabsList[componentA.GetID()];
                        return true;
                    }
                    else
                    {
                        componentResult = objectsPrefabsList[componentB.GetID()];
                        return true;
                    }
                }
            }
        }
        return false;
    }




}

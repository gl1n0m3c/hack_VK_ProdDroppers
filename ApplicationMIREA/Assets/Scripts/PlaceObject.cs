using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;
using UnityEngine.XR.ARSubsystems;
using EncancedTouch = UnityEngine.InputSystem.EnhancedTouch;

[RequireComponent(typeof(ARRaycastManager), typeof(ARPlaneManager))]
public class PlaceObject : MonoBehaviour
{
    [SerializeField]
    private GameObject prefab0;
    [SerializeField]
    private GameObject prefab1;
    [SerializeField]
    private GameObject prefab2;

    private ARRaycastManager aRRaycastManager;
    private ARPlaneManager aRPlaneManager;
    private List<ARRaycastHit> hits = new List<ARRaycastHit>();

    private void Awake()
    {
        aRRaycastManager = GetComponent<ARRaycastManager>();
        aRPlaneManager = GetComponent<ARPlaneManager>();
    }

    private void OnEnable()
    {
        EncancedTouch.TouchSimulation.Enable();
        EncancedTouch.EnhancedTouchSupport.Enable();
        EncancedTouch.Touch.onFingerDown += FingerDown;
    }

    private void OnDisable()
    {
        EncancedTouch.TouchSimulation.Disable();
        EncancedTouch.EnhancedTouchSupport.Disable();
        EncancedTouch.Touch.onFingerDown -= FingerDown;
    }

    private void FingerDown(EncancedTouch.Finger finger)
    {
        if (finger.index != 0) return;

        if (aRRaycastManager.Raycast(finger.currentTouch.screenPosition, hits, TrackableType.PlaneWithinPolygon))
        { 
            foreach (ARRaycastHit hit in hits)
            {
                Pose pose = hit.pose;
                GameObject[] prefabs = { prefab0, prefab1, prefab2 };
                GameObject obj = Instantiate(prefabs[Random.Range(0, prefabs.Length)], pose.position, pose.rotation);
            }
        }
    }
}

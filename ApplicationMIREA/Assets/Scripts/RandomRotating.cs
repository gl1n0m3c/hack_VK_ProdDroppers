using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RandomRotation : MonoBehaviour
{
    public float rotationSpeed = 5f;

 
    void Update()
    {
        float randomAngleX = 0;
        float randomAngleY = Random.Range(0f, 360f);
        float randomAngleZ = Random.Range(0f, 360f);

        Quaternion randomRotation = Quaternion.Euler(randomAngleX, randomAngleY, randomAngleZ);

        transform.rotation = Quaternion.RotateTowards(transform.rotation, randomRotation, rotationSpeed * Time.deltaTime);
    }
}
# UE4 basics
###### tags: `unrealcv`, `UE4`

## Convert FString to number?

`FCString::Atoi(*Args[0]);`

[Lighting](http://mp.weixin.qq.com/s/_5HagOdYslzrsmd5yvCLaw)

Can I change the default project location?

[discussion1](https://answers.unrealengine.com/questions/64496/how-can-i-change-the-default-location-of-unreal-pr.html)
[discussion2](https://answers.unrealengine.com/questions/12526/change-default-location-of-unreal-projects.html)


## Get an actor by ID

```C++
FString ModelId = TEXT("");
UWorld* World = ;
for (TActorIterator<AActor> ActorItr(World); ActorItr; ++ActorItr)
{
    AActor* Actor = *ActorItr;
    if (Actor->GetName() == ModelId)
    {
        break;
    }
}
```
---
__Let's Learn Some Basic GitHub Steps :)__

- __[KOMEN.CO](https://www.komen.co.in/)__ -The Beginning of your Journey
![Minion](https://user-images.githubusercontent.com/16015962/109482637-3e194200-7aa4-11eb-920e-0dc7aa891e1b.png)

__Following are basic GitHub Steps!__

---
## Steps:
`code`

 0 step: Switch to the local main branch

    git checkout main
    //if switch to branch then main-->[branchmain];


1 step: Sync to the main branch:
```
git pull origin main
```

2 step: Create a new branch & checkout(shift local to that branch) the same

``` 
git branch [branchname(format:UserName/FeatureName)]
git checkout [branchname]
                     OR
//alternative to above two;
git checkout -b [branchname]
```


3 step: Make changes & verify then stage the file
 
To verify
``` 
git diff
  OR
git status
``` 
To stage
``` 
git add ./[filename(that created/changed)]

  OR
(if all the changes need to be staged)

git add . 
```

4 step(optional): Check the status & verify the file has been staged

``` 
git status
```

5 step: commit the change with a meaningful message(recommended) to your local

``` 
git commit -m "your commit message"
```
6 step: push the changes to the remote repository

``` 
git branch [branchname(format:UserName/FeatureName)]
git checkout [branchname]
```


*Thanks!!  [Visit Us](https://www.komen.co.in/)*

---
![Minion](https://user-images.githubusercontent.com/16015962/109482637-3e194200-7aa4-11eb-920e-0dc7aa891e1b.png)

__[Komenco](https://www.komen.co.in/)__ -The Beginning of your Journey

__Following are the steps to get started with git!__

---
## Steps:

 1. Switch to the local main branch
    ```
    git checkout main
    //if switch to branch then main-->[branchmain];
    ```


2. Sync to the main branch:
    ```
    git pull origin main
    ```

3. Create a new branch & checkout(shift local to that branch) the same

    ``` 
    git branch [branchname(format:UserName/FeatureName)]
    git checkout [branchname]
    ```
    -----OR-----
                        
    ```
    //alternative to above two;
    git checkout -b [branchname]
    ```


4. Make changes & verify then stage the file
 
    To verify
    ``` 
    git diff
    ```
    -----OR-----
                        
    ```
    git status
    ``` 
    To stage
    ``` 
    git add ./[filename(that created/changed)]
    ```
    -----OR-----
                        
    (if all the changes need to be staged)
    ```
    git add . 
    ```
5. [Optional] Check the status & verify the file has been staged

    ``` 
    git status
    ```

6. commit the change with a meaningful message(recommended) to your local
    ``` 
    git commit -m "your commit message"
    ```
7. push the changes to the remote repository
    ``` 
    git push origin [branchname]
    // switch back to main
    git checkout main
    ```


*Thanks!  Visit us at [komen.co.in](https://www.komen.co.in/)*

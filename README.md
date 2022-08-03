# RandTake
A cli tool to randomly generating sample data from a folder. It is file format agnostic so you can be sure that it will work for any kind of data be it jpeg, mp3 or anything else.

#### Lets come to the usage
In the `dist` directory you can have the windows app called `randtake.exe`.

Now, goto the folder that holds the folder in which the data are kept.
Lets say we have a folder called `amit` and within that folder other folders are kept from which we want to collect samples,
```
amit/
    image/
    audio/
    video/
```
>Assume our task is to take 10 random samples from each folder and put that to a folder called `selected`.
Then, just open the powershell in that folder.
Type `.\randtake.exe --help` to see the usage.
General Syntax is as follows,
```
.\randtake --input <folder_having_data> --output <folder_name_you_want> --size <size_of_the_input> --seed <optional_seed_value>
```

>Solution to our task is:
```
.\randtake --input image --output selected --size 10 --seed 2
.\randtake --input audio --output selected --size 10 --seed 2
.\randtake --input video --output selected --size 10 --seed 2
```
So this way you can actually automate and speed up your workflow.

Disclaimer: This version uses pyinstaller so it produces huge binary and it is comparatively slower. But guess what I will make up this shortcoming with a similar tool which will be far faster and better.
Stay Tunned.
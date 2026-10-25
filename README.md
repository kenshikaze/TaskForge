# TaskForge

![image alt](logo.png)

-It is a simple todo list, that runs in a Linux terminal. <br>
-*Other Operating systems are still untested.*

-It can be run from the **source**, and a **prebuilt Linux executable** is available for users who don't want to set up Python manually.

## Installation
-As stated in description, it can run in both ways(*from source & from Linux executable*)

## Using source(Way 1)
**Prerequisites:-** Python 3.12(*tested*) and git

1.Clone the repo:-
```bash
git clone https://github.com/kenshikaze/TaskForge
```

2.Navigate to project:-
```bash
cd Taskforge 
```

3. Install the required dependencies:-
```bash 
pip install -r requirements.txt
```

## Using prebuilt Linux executable

1.Open the project's Github releases page:-
```bash
https://github.com/kenshikaze/TaskForge/releases/tag/v0.1.0
```

2.Download the TaskForge executable from the release assets.
3.Open a terminal in the directory containing the download file.
4.Give the file permission to execute:
```bash
chmod +x TaskForge
```
5. Check how it works:
```bash
./TaskForge --help
```

-You can run commands using **./TaskForge** .

## Usage
Run TaskForge in the project directory:-
**Python source:-**
```bash
python taskforge.py --help
```
**Prebuilt Executive:-**
```bash
./TaskForge --help
```

-To view help for specific command:-
**Python source:-**
```bash
python taskforge.py <command> --help
```
**Prebuilt executable:-**
```bash
./TaskForge --help
```

-It has 3 in-built categories(*for tasks*):-
1.Coding
2.Study
3.Personal

## Commands
It has Six commands:-
(These all are the syntax for commands to run when the you go with way 1,<br>
-Replace **python taskforge.py** with **./TaskForge** to use the commands in Linux executable.)
1.**add :-**
```bash
python taskforge.py add "<task>" "<category>"
```

2.**delete :-**
```bash
python taskforge.py delete <position>
```

3.**update :-**
```bash
python taskforge.py update <position> --task "<task>" --category "<category>"
```
*task and category are optional<br>
(*chose what you want to update*)

4.**complete :-**
```bash
python taskforge.py complete <position>
```
5.**show :-**
```bash
python taskforge.py show --status <1/2>
```
*status is optional<br>
(*1 = pending tasks ; 2 =complete tasks*)

6.**stats :-**
```bash
python taskforge.py stats
```

-Tasks are stored locally in a file named **tasks.db**,which will be created automatically when needed.

## Limitations
-Only tested in Linux(Codespaces)
-The executable is a terminal application, not a graphical desktop application.

## Contributer
Made by Kaze(kenshikaze)
# TaskForge

![image alt](logo.png)

It is a simple todo list, that runs in a terminal across Linux(*tested*),Windows,etc.<br>

## Installation
**Prerequisities:-** Python 3.x and git

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

## Usage
Run TaskForge in the project directory:-
```bash
python taskforge.py --help
```

*view help for specif command*
```bash
python taskforge.py <command> --help
```

## Commands
It has Four commands:-
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
*task and category are optional*

4.**complete :-**
```bash
python taskforge.py complete <position>
```

## Contibuter
Made by Kaze(kenshikaze)
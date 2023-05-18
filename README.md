# Crystal CMD

Crystal CMD is a powerful command-line environment that provides a range of features and functionalities to enhance your command-line experience.

## Features
- **Image Display**: Crystal CMD allows you to display images directly in the terminal. It supports various image formats and provides options for resizing and preserving aspect ratios.

- **Command Execution**: Execute commands and scripts directly within the Crystal CMD environment. Run your favorite command-line tools and scripts without leaving the terminal, using *run* comand, to run any comand, from sudo, to wine(untested)

- **Tab Completion**: Take advantage of tab completion to speed up your workflow. Crystal CMD provides intelligent tab completion for commands

- **History and Navigation**: Easily navigate through your command history and use keyboard shortcuts for efficient command recall and editing.

## Installation

Crystal CMD can be installed by following these steps:

1. Clone the Crystal CMD repository from GitHub:

   ```shell
   git clone https://github.com/cross-sans2/crystal-cmd/
   ```
2. Run 'python main.py' to make sure you have the nessessary dependencies to run the cmd, then make sure to have pyinstaller(pip install pyinstaller) then run
	```shell
	make
	```
	And wait until its finished compiling, then a new gnu-terminal window should open with the Crystal cmd open

3. Making it be default(optional, not recomended)
 todo: make the guide


# updating
Just go to the github repo and download the main.py(and any new file there).
Then place it in the same folder as a older version, and run
```shell
make
```
again, it should update your Crystal cmd, however, as things thend to not go smoothly, make sure you have a backup, or a way of removing Crystal cmd from being the default terminal
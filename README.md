# Surround

This is a simple plugin which surrounds all selected text pieces by a given HTML tag.

## Install

### Package Control

If you haven't installed Package Control yet, visit [Official installation guide](https://packagecontrol.io/installation).

Once **Package Control** is installed, you have to press ```Ctrl+shift+p``` and select the **Package Control: Install Package** option.

A list of plugins will show up. Type **Surround** and select it from the list. It will automatically install and keep updated. You are done!

## Usage

Select some text (you can select more than one piece of text) and press ```Ctrl+Shift+M```. Write in the prompt the desired tag WITHOUT < and >. You can even add some styling. Press ```Enter``` to surround the text with the given tag.

### Example

Given the selected text
```
Hi There
``` 
writing in the prompt
```span style="color:blue"```
will result in
```
<span style="color:blue">Hi There</span>
```
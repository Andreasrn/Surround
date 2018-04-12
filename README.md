# Surround

This is a simple plugin which surrounds all selected text pieces by a given HTML tag.

## Getting Started

### Using Git
Go to your Sublime Text 3 ```Packages``` directory and clone this repository using this command:
```git clone https://github.com/Andreasrn/Surround.git```

### Manually
Download these files and place them in your Sublime Text 3 Packages directory.

## Usage

Select some text (you can select more than one piece of text) and press ```Ctrl+Shift+M```. Write in the prompt the desired tag WITHOUT < and >. You can even add some styling. Press ```Enter``` to surround the text with the given tag.

### Example

Given the selected text ```Hi There``` , writing in the prompt ```span style="color:blue"``` will result in
```<span style="color:blue">Hi There</span>```
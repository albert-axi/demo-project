#!/usr/bin/env python3
from helpers import main_menu, prompt_input, render

def main():
  print("Welcome to My Playlist App!")
  main_menu()
  value = prompt_input()
  
  while(not value):
    value = prompt_input()
    
  render(value)
  
  
main()
  
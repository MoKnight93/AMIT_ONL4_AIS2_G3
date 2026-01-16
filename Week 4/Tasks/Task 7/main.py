from ui.console_ui import run_console
from ui.gui_tkinter import run_gui

def main():
    """Main entry point - choose interface."""
    print("\n" + "="*50)
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("="*50)
    print("Choose interface:")
    print("1. Console (Text-based)")
    print("2. GUI (Desktop App)")
    print("3. Dashboard (Web Browser - run manually)")
    print("4. Exit")
    print("="*50)
    
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        run_console()
    elif choice == '2':
        run_gui()
    elif choice == '3':
        print("\nTo run the dashboard, use this command: ")
        print("streamlit run dashboard_streamlit.py\n")
    elif choice == '4':
        print("Exiting... Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        run_console()


if __name__ == "__main__":
    main()
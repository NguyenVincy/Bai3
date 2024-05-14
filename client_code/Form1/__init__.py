from ._anvil_designer import Form1Template
from anvil import *
import time

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Add sorting algorithms to the dropdown
        self.drop_down_1.items = [
            ("Insertion Sort", "insertion"),
            ("Selection Sort", "selection"),
            ("Bubble Sort", "bubble"),
            ("Merge Sort", "merge")
        ]

    def drop_down_1_change(self, **event_args):
        """This method is called when an item is selected"""
        pass

    def text_box_2_pressed_enter(self, **event_args):
        """This method is called when the user presses Enter in this text box"""
        pass

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Get the selected algorithm and data
        algorithm = self.drop_down_1.selected_value
        data = self.text_box_2.text
        
        # Convert input data to a list of integers
        try:
            data_list = list(map(int, data.split(',')))
        except ValueError:
            alert("Invalid input. Please enter a list of integers separated by commas.")
            return

        # Display the initial data
        self.display_initial_data(data_list)

        # Apply the selected sorting algorithm
        if algorithm == "insertion":
            sorted_data = self.insertion_sort(data_list)
        elif algorithm == "selection":
            sorted_data = self.selection_sort(data_list)
        elif algorithm == "bubble":
            sorted_data = self.bubble_sort(data_list)
        elif algorithm == "merge":
            sorted_data = self.merge_sort(data_list)
        else:
            alert("No algorithm selected.")
            return

        # Display the sorted data
        self.display_sorted_data(sorted_data)

    def display_initial_data(self, data):
        # Clear previous squares
        self.data_row_panel_1.clear()

        # Display squares for each number
        for num in data:
            square = Label(text=str(num), align='center')
            square.background = '#34eb67'  # Blue color
            square.height = 40
            square.width = 40
            self.data_row_panel_1.add_component(square)

    def display_sorted_data(self, data):
        # Clear previous squares
        self.data_row_panel_1.clear()

        # Display squares for each number
        for num in data:
            square = Label(text=str(num), align='center')
            square.background = '#eb3434'  # Red color
            square.height = 40
            square.width = 40
            self.data_row_panel_1.add_component(square)

            # Pause to visualize each step
            time.sleep(0.5)

    def insertion_sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

    def selection_sort(self, data):
        for i in range(len(data)):
            min_idx = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
        return data

    def bubble_sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    def merge_sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1
        return data

    def plot_1_click(self, points, **event_args):
        """This method is called when a data point is clicked."""
        pass

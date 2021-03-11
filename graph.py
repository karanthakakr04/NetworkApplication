from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


# To list all available pre-defined styles use: print(plt.style.available)
plt.style.use('fivethirtyeight')  # Customizing Matplotlib with pre-defined style(s)

# In matplotlib there are two ways to create plots: using procedural methods and using object-oriented approach.
# To allow more customization, we need to move to a more object-based way to make the plots. This method involves
# storing various elements of the of the plots in variables (these are objects in object-oriented terminology).
# Creating a new figure
fig = plt.figure()

# The second line creates subplot on a 1x1 grid. As we described before, the arguments for add_subplot are the number of
# rows,columns, and the ID of the subplot, between 1 and the number of columns times the number of rows.
ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
# NOTE: We’re going to create a subplot to make it easier for us to draw on the same plot over and over again.


# Creating a function that reads the data from cpu.txt and feeds it to our subplot
def animation_frame(i):
    # Creating an empty list in which to append each value in the file converted from string to float
    cpu_utilization = []

    # Opening the file and reading each row of CPU utilization data in the file; creating a list of values
    # NOTE: When you don't specify the file operation it is by default 'r'
    cpu_data = open(r'/home/karan/PycharmProjects/NetworkApp/cpu.txt', encoding='utf-8').read().splitlines()  # Get the data
    for value in cpu_data:
        # Iterating over the list of CPU values and appending each value (converted to float) to the previously
        # created list - x; adding an if statement to exclude any blank lines in the file
        if len(value) > 1:
            cpu_utilization.append(float(value))

    # Clearing/Refreshing the axis to avoid unnecessary overwriting for each new poll (every 10 seconds) to build the
    # graph
    ax.clear()  # The Axes.clear() function in axes module of matplotlib library is used to clear the axes.

    ax.plot(cpu_utilization, label='Arista1')  # Plotting the values in the list
    # We have also set a 'label' here which is going to be automatically picked up by legend()

    # The elements to be added to the legend are automatically determined, when you do not pass in any extra arguments.
    ax.legend(loc='upper right')  # Place a legend on the axes.

    ax.set_title('Arista1')  # Method to Add Title to Subplot(s) in Matplotlib

    ax.set_xlabel('Time')  # Set the label for the x-axis.
    ax.set_ylabel('CPU Utilization')  # Set the label for the y-axis.
    # ax.tight_layout()


# Using the figure, the function and a polling interval of 10000 ms (10 seconds) to build the graph
animation = FuncAnimation(fig, func=animation_frame, interval=10000)  # Makes an animation by repeatedly calling a
# function func, in this case, animation_frame().

plt.tight_layout()  # Adjust the padding between and around subplots.

plt.show()  # Displaying the graph to the screen

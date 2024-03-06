import matplotlib.pyplot as plt

def main():
    
    chart_title = input("Enter the bar graph title: ")

    
    x_label = input('Enter the label for the x-axis: ')
    y_label = input('Enter the label for the y-axis: ')

    
    points = int(input('Enter the number of data points: '))

    values = []
    names = []

    
    for i in range(points):
        names.append(input(f'Enter the name for tick {i + 1} : '))
        values.append(float(input(f'Enter the value for tick {i + 1} : ')))
    
    plt.bar(values,names)
    plt.title(chart_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

main()
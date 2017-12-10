import csv
import numpy as np
import matplotlib.pyplot as plt
import math

def classify_bikes():
    with open('../datasets/bikes_filtered.csv', 'r') as f1:
        datareader = csv.reader(f1)
        with open('../datasets/bikes_classified.csv', 'w') as f2:
            datawriter = csv.writer(f2)
            bike25 = []
            bike50 = []
            bike75 = []
            bike100 = []
            for data in datareader:
                price = int(data[2])

                if price < 500:
                    data.append(25)
                    bike25.append(price)
                elif price < 1000:
                    data.append(50)
                    bike50.append(price)
                elif price < 2500:
                    data.append(75)
                    bike75.append(price)
                else:
                    data.append(100)
                    bike100.append(price)

                datawriter.writerow(data)
            print('Num of bikes in 0-25 percentile: ' + str(len(bike25)))
            print('Num of bikes in 25-50 percentile: ' + str(len(bike50)))
            print('Num of bikes in 50-75 percentile: ' + str(len(bike75)))
            print('Num of bikes in 75-100 percentile: ' + str(len(bike100)))

            bike25_avg = float(np.sum(np.array(bike25)))/len(bike25)
            bike50_avg = float(np.sum(np.array(bike50)))/len(bike50)
            bike75_avg = float(np.sum(np.array(bike75))) / len(bike75)
            bike100_avg = float(np.sum(np.array(bike100))) / len(bike100)

            print('Avg bike price in 0-25 percentile: ' + str(bike25_avg))
            print('Avg bike price in 25-50 percentile: ' + str(bike50_avg))
            print('Avg bike price in 50-75 percentile: ' + str(bike75_avg))
            print('Avg bike price in 75-100 percentile: ' + str(bike100_avg))

def classify_cars():

    with open('../datasets/cars_filtered.csv', 'r') as f1:
        datareader = csv.reader(f1)
        with open('../datasets/cars_classified.csv', 'w') as f2:
            datawriter = csv.writer(f2)
            cars20 = []
            cars40 = []
            cars60 = []
            cars80 = []
            cars100 = []
            for data in datareader:
                price = int(data[3])

                if price < 25000:
                    data.append(20)
                    cars20.append(price)
                elif price < 35000:
                    data.append(40)
                    cars40.append(price)
                elif price < 45000:
                    data.append(60)
                    cars60.append(price)
                elif price < 65000:
                    data.append(80)
                    cars80.append(price)
                else:
                    data.append(100)
                    cars100.append(price)

                datawriter.writerow(data)
            print('Num of cars in 0-20 percentile: ' + str(len(cars20)))
            print('Num of cars in 20-40 percentile: ' + str(len(cars40)))
            print('Num of cars in 40-60 percentile: ' + str(len(cars60)))
            print('Num of cars in 60-80 percentile: ' + str(len(cars80)))
            print('Num of cars in 80-100 percentile: ' + str(len(cars100)))

            cars20_avg = float(np.sum(np.array(cars20))) / len(cars20)
            cars40_avg = float(np.sum(np.array(cars40))) / len(cars40)
            cars60_avg = float(np.sum(np.array(cars60))) / len(cars60)
            cars80_avg = float(np.sum(np.array(cars80))) / len(cars80)
            cars100_avg = float(np.sum(np.array(cars100))) / len(cars100)
            #print(cars20_avg, cars40_avg, cars60_avg, cars80_avg, cars100_avg)
            print('Avg car price in 0-20 percentile: ' + str(cars20_avg))
            print('Avg car price in 20-40 percentile: ' + str(cars40_avg))
            print('Avg car price in 40-60 percentile: ' + str(cars60_avg))
            print('Avg car price in 60-80 percentile: ' + str(cars80_avg))
            print('Avg car price in 80-100 percentile: ' + str(cars100_avg))


def analysis():
    bike_data_array = []
    with open('../datasets/bikes_filtered.csv', 'r') as f:
        datareader = csv.reader(f)
        for data in datareader:
            data_sub = [data[0], data[1], int(data[2])]
            bike_data_array.append(data_sub)
        bike_data_array.sort(key=lambda x: x[2])
        #print(len(bike_data_array))


    car_data_array = []
    with open('../datasets/cars_filtered.csv', 'r') as f:
        datareader = csv.reader(f)
        for data in datareader:
            data_sub = [data[0], data[1], data[2], int(data[3])]
            car_data_array.append(data_sub)
        car_data_array.sort(key=lambda x: x[3])

        #print((car_data_array))

    bike_prices = np.zeros(len(bike_data_array))
    bike_log_prices = np.zeros(len(bike_data_array))

    for i, bike in enumerate(bike_data_array):
        bike_prices[i] = bike[2]
        bike_log_prices[i] = math.log(bike[2])
        #plt.show()
        pass

    car_prices = np.zeros(len(car_data_array))
    car_log_prices = np.zeros(len(car_data_array))

    for i, car in enumerate(car_data_array):
        car_prices[i] = car[3]
        car_log_prices[i] = math.log(car[3])
        pass

    '''
    plt.plot(bike_prices)
    plt.show()
    plt.plot(bike_log_prices)
    plt.show()
    plt.plot(car_prices)
    plt.show()
    plt.plot(car_log_prices)
    plt.show()
    '''

    print(np.percentile(bike_prices, 25))
    print(np.percentile(bike_prices, 50))
    print(np.percentile(bike_prices, 75))

    print('by 20')
    print(np.percentile(car_prices, 20))
    print(np.percentile(car_prices, 40))
    print(np.percentile(car_prices, 60))
    print(np.percentile(car_prices, 80))


    def cdf(data):

        data_size=len(data)

        # Set bins edges
        data_set=sorted(set(data))
        bins=np.append(data_set, data_set[-1]+1)

        # Use the histogram function to bin the data
        counts, bin_edges = np.histogram(data, bins=bins, density=False)

        counts=counts.astype(float)/data_size

        # Find the cdf
        cdf = np.cumsum(counts)

        # Plot the cdf
        #plt.plot(bin_edges[0:-1], cdf,linestyle='--', marker="o", color='b')
        plt.plot(bin_edges[0:-1], cdf)#,linestyle='--', marker="o", color='b')

        print((bin_edges[5]))
        plt.ylim((0,1))
        plt.ylabel("CDF")
        plt.grid(True)

        plt.show()

    cdf(bike_prices)

    cdf(car_prices)

def main():
    #analysis()
    classify_bikes()
    classify_cars()


if __name__ == '__main__':
    main()

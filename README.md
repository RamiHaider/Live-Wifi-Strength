Real Time View of your Wifi Signal Strength for Mac OS

For Macbook OS, you can hold the 'option' button on your keyboard and select the wifi icon located at the top, and you'll get wifi metrics that updates once every second.
<a href="https://ibb.co/cLVHmzb"><img src="https://i.ibb.co/3zQqJtf/Frame-32.png" alt="Frame-32" border="0"></a>
However, there's no built in way to view that in a time series way (with time on the x axis and the values on the y).
There does exists Apps to do that, but none of them are free. Here is a free way
that will look like this:
<a href="https://ibb.co/k927x1y"><img src="https://i.ibb.co/k927x1y/Screenshot-2024-05-25-at-9-50-33-PM.png" alt="Screenshot-2024-05-25-at-9-50-33-PM" border="0"></a>

It works by using the CoreWLAN framework and outputting the fetched data to a .txt
Then liveplots the 250 most recent datapoints using the Ipython.display feature from matplotlib

How to do this?

Simply download both .py (ONe is meant for fetching the data, the other for plotting) put them in the jupyter notebook directory.
Since, in Jupyter Notebooks you are unable to run two simultaneously running cells at the same time, my trick is open a terminal
run: python Collect_and_Export_Wifi_Metrics.py
this runs that code above
Then in the anaconda, or even another terminal run the PLotting code. Ta da

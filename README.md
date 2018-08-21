# SPC-Conv-Forecast
## Example
Sample Day 1 SPC Forecast: (05/18/2017 1200Z Day 1 Forecast) ![picture alt](https://raw.githubusercontent.com/tmaldrsn/SPC-Conv-Forecast/v0.3.4/2017-05-18_1200_UTC_Day_1_convective_outlook%20(1).gif "SPC Day 1 05/18/2017 1200Z Forecast")

    
Snippet of text file associated with the forecast:  
![picture alt](https://raw.githubusercontent.com/tmaldrsn/SPC-Conv-Forecast/v0.3.4/text_forecast.png "Raw Forecast Snippet")    
Each 8 digit code is associated with a latitude-longitude coordinate, or an indication of continuation from one point on the border to another point somewhere else on the border, and represents a vertex of the polygon in the figure.


Associated plot from plot_categorical.py script:  
![picture alt](https://raw.githubusercontent.com/tmaldrsn/SPC-Conv-Forecast/v0.3.4/Figure_1.png "Reproduced forecast figure")


Similar plots for the following events and day outlooks can be created as according to the table below:  

| Event | Day 1 | Day 2 | Day 3 | Days 4-8 |
|:-----:|:-----:|:-----:|:-----:|:--------:|
| Categorical | X | X | X | |
| Tornado | X | | | |
| Wind | X | | | |
| Hail | X | | | |
| Severe | | X | X | X |


# Change Log
### Current Version: 0.3
  * Implement Day 2, 3, 4-8 outlooks
    * Added categorical / severe probability plotting for days 2 & 3
    * Added separate plotting for days 4-8 forecast
  * Ability to import text files from previous forecasts
  * Added forecast text file lookup
  
#### Goals for v0.4:
  * Figure out early morning forecast schedule (0600, 1200 forecast timing)
  * Investigate old SPC forecast format and date cutoff
    * old forecasts in day 1 don't include marginal & enhanced categories
  * Start writing script to detemine if coordinates lie in given categories
  * Use Tkinter library to create a GUI related to the API

### Previous Versions:     

#### Version: 0.2
 * Eliminated need for JSON file handling by using arrays for each line
 * Using shapely library to plot probability boundaries
   * https://pypi.org/project/Shapely/
 * Goes to SPC website and pulls most recently available Day 1 convective outlook
 * Plotting capabilities using matplotlib library and shapely library
   * Four separate plotting scripts ==> Tornado, Hail, Wind and Categorical probabilities
   * Uses information from 2010 census to plot contiguous US boundaries
     * https://www.census.gov/geo/maps-data/data/cbf/cbf_nation.html

#### Version 0.1:
  * Pulling most recent [Day 1 convective outlook](http://www.spc.noaa.gov/products/outlook/) from SPC
    * ~~Saving text file in json format:~~
      * ~~Currently fixing bug where coordinates are in unordered format~~
  * ~~Finds most recent json file in data folder and determines whether a set of coordinates is in any event/probability combination~~
    * ~~Bug where discontinuation in json coordinates (see above) leads to false outcomes~~
  * Shell script that determines time and whether or not a new forecast has been released
    * Very basic shell script, not much functionality

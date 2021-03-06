# SPC-Conv-Forecast
## Example
Sample Day 1 SPC Forecast: (05/18/2017 1200Z Day 1 Forecast) ![picture alt](https://raw.githubusercontent.com/tmaldrsn/SPC-Conv-Forecast/master/img/2017-05-18_1200_UTC_Day_1_convective_outlook.gif "SPC Day 1 05/18/2017 1200Z Forecast")


Snippet of text file associated with the forecast:  
![picture alt](https://raw.githubusercontent.com/tmaldrsn/SPC-Conv-Forecast/master/img/text_forecast.png "Raw Forecast Snippet")    
Each 8 digit code is associated with a latitude-longitude coordinate, or an indication of continuation from one point on the border to another point somewhere else on the border, and represents a vertex of the polygon in the figure.


Associated plot from plot_categorical.py script:  
![picture alt](https://raw.githubusercontent.com/tmaldrsn/SPC-Conv-Forecast/master/img/Figure_1.png "Reproduced forecast figure")


Similar plots for the following events and day outlooks can be created as according to the table below:  

| Event | Day 1 | Day 2 | Day 3 | Days 4-8 |
|:-----:|:-----:|:-----:|:-----:|:--------:|
| Categorical | X | X | X | |
| Tornado | X | | | |
| Wind | X | | | |
| Hail | X | | | |
| Severe | | X | X | X |


# Change Log
### Current Version: 0.4
  * Cleaned up much of the codebase, including condensing five separate plotting scripts into a single script
  * Created basic Tkinter GUI allowing for simple forecast lookup, only for most recent forecast so far
  
#### Goals for v1.0:
  * Forecast lookup for any past archived outlook, with GUI support
  * (maybe) Determining the set of risks for severe weather given a coordinate
  * Optimize the code for efficiency and readability
  * Provide GUI and command line support
  * Add tutorial to README

### Previous Versions:     
#### Version: 0.3
  * Implement Day 2, 3, 4-8 outlooks
    * Added categorical / severe probability plotting for days 2 & 3
    * Added separate plotting for days 4-8 forecast
  * Ability to import text files from previous forecasts
  * Added forecast text file lookup

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

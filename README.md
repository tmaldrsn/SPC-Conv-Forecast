# SPC-Conv-Forecast

## Current Version: 0.3
  * Implement Day 2, 3, 4-8 outlooks
    * Added categorical / severe probability plotting for days 2 & 3
    * Added separate plotting for days 4-8 forecast
  * Ability to import text files from previous forecasts
  * Added forecast text file lookup
  
### Goals for v0.4:
  * Figure out early morning forecast schedule (0600, 1200 forecast timing)
  * Investigate old SPC forecast format and date cutoff
    * old forecasts in day 1 don't include marginal & enhanced categories
  * Start writing script to detemine if coordinates lie in given categories
  * Use Tkinter library to create a GUI related to the API

## Previous Versions:     

### Version: 0.2
 * Eliminated need for JSON file handling by using arrays for each line
 * Using shapely library to plot probability boundaries
   * https://pypi.org/project/Shapely/
 * Goes to SPC website and pulls most recently available Day 1 convective outlook
 * Plotting capabilities using matplotlib library and shapely library
   * Four separate plotting scripts ==> Tornado, Hail, Wind and Categorical probabilities
   * Uses information from 2010 census to plot contiguous US boundaries
     * https://www.census.gov/geo/maps-data/data/cbf/cbf_nation.html

### Version 0.1:
  * Pulling most recent [Day 1 convective outlook](http://www.spc.noaa.gov/products/outlook/) from SPC
    * ~~Saving text file in json format:~~
      * ~~Currently fixing bug where coordinates are in unordered format~~
  * ~~Finds most recent json file in data folder and determines whether a set of coordinates is in any event/probability combination~~
    * ~~Bug where discontinuation in json coordinates (see above) leads to false outcomes~~
  * Shell script that determines time and whether or not a new forecast has been released
    * Very basic shell script, not much functionality

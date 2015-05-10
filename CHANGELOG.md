Change Log for GHG Monitoring Tower Program
===========================================

Next release
------------

### Issues Fixed

* Use min/max battery & temperature data from `site_daily` table, as intended,
  instead of -7999/PanelTemp/Battery values in daily update email

### Data Table Changes

* New column `GitRepoTag` in the `site_info` table, after `ProgSig`


v1.0 (2015-05-08)
-----------------

> <div style="border: 1px solid red; padding: 4px">**Security advisement**  
> A minimum of level 1 datalogger security is **required** for safe operation
> of this program. If no security level is set, potentially catastropohic
> changes can be made by anonymous users![^1]</div>

  [^1]: In reality, seriously damaging changes can be made by anonymous users
        even in previous versions; however, with this release *only* settings
        and debug values are exposed in the Public table and the risk of
        unintentional changes is higher.

> <div style="border: 1px solid red; padding: 4px">**New include file**  
> Before deployment, an encrypted version of the email include file **must** 
> be stored on the logger's `CPU` drive.</div>

> <div style="border: 1px solid red; padding: 4px">**Incompatible settings file**  
> After deployment, program settings must be **completely reset** before
> reprogramming with site-specific values.</div>


### Known Issues

* *Required actions before deployment*
    * Enable datalogger security at Level 1 or higher
    * Update template `email-template.cr3` as appropriate, then use CRBasic
      Editor's 'Save and Encrypt...' option to save as `email_Enc.cr3`
    * Send `email_Enc.cr3` to the datalogger's CPU drive. Do **not** set 
      'Run now' or 'Run on startup' options when pushing this file
* *Required actions after deployment*
    * Reset program settings (or delete settings file from CPU drive) and
      re-program with correct site-specific values


### Enhancements

* Transition back to conditional compilation for auxiliary sensors:
  Decagon NDVI/PRI radiometers, Los Gatos N2O/CO, Picarro CO2/CH4, Huskeflux
  soil heat flux plate
    * No longer produces empty tables if sensors are not used (solves problem
      with CardConvert halting for user interaction when empty tables are
      encountered, improving automation scripts)
    * Increase available recording time by not allocating space for sensors
      which are not used
    * Can only be changed via 'Initial setup' menu or ConstTable; triggers
      recompilation
* Use boolean settings to enable/disable: cup and vane wind set, rain gage,
  soil moisture probes
    * Data tables are unchanged but if disabled, only NANs are recorded
    * Can be modified via 'Settings' menu or Public table; made effective
      by changing `save_changes` to True
* Expose program settings ("Settings" logger menu) values in Public table
  along with variable to save/apply settings
    * Allows remote modification of settings via LoggerNet Connect screen
    * Reduces memory consumption because of fewer variables being cached
      for public display
* Notify by email when program starts up or whenever test email is sent
* Exclude known-bad data from PAR sensor (0 or negative voltages)


### Other Changes

* Variables can no longer be monitored in the Public since it's repurposed for
  remote settings access
* New datalogger menu structure
    * previous top-level menu items are now under 'System Menu' submenu
    * previous 'Sensor Setup' submenu is now 'Settings' submenu
    * new submenu 'Initial Setup' contains options to enable/disable auxiliary
      sensors (described under *Enhancements* above)


20140616_MMTN
-------------

### Other Changes

* Revert PAR sensor signal input location back: DF 6 -> DF 5
* Update MMTN datalogger serial number to reflect fact physical datalogger
  unit (S/N 6504) was exchanged with current spare (S/N 6506)


20140610_MMTN
-------------

### Issues Fixed

* Update sensitivity value for PAR sensor, which was exchanged May 6, 2014:
  previous sensor (Q45241) value 6.69 -> 6.03 of current sensor (Q45933)

### Other Changes

* Change input channel of PAR sensor (LI190SB) DF 5 -> DF 6; also add to
  ConstTable to facilitate in-field investigation/troubleshooting


20140217_XXXX
-------------

### Other Changes

* Remove reviewer-flag from program source code comments


20131018_XXXX
-------------

### Issues Fixed

* Remove duplicate suffix from column 'CO2_ppm_Avg_Avg' -> 'CO2_ppm_Avg'

### Other Changes

* Internally, change handling of sonic & IRGA diagnostic flags
* Discard temperature and do not calculate volumetric water content if 
  dielectric value from soil moisture probes is null ("NAN")


20131012_CFNT
-------------

### Known Issues

* Duplicate suffix column remains ('CO2_ppm_Avg_Avg')

### Other Changes

* Attempt to enable Los Gatos N2O/CO by editing default value within subroutine
  `set_default_choices()`


20130711_MSLK
-------------

### Issues Fixed

* Correct sonic azimuth 245 -> 254

### Known Issues

* Duplicate suffix column remains ('CO2_ppm_Avg_Avg')


20130619_MSLK
-------------

### Issues Fixed

* Correct array length declaration  (4 -> 2) for variable `dec_ndvi_up`; this
  is a cosmetic fix

### Known Issues

* Sonic azimmuth is incorrectly specified as 245 instead of 254
* Duplicate suffix column remains ('CO2_ppm_Avg_Avg')

### Enhancements

* Add site-specific values for new monitoring site in Moses Lake, WA
* Move save confirmation within 'Sensor Setup' menu into submenu

### Other Changes

* When Decagon NDVI/PRI sensors are inactive, set data destinations to null
  values ("NAN") only once instead of each scan


20130507_XXXX
-------------

### Issues Fixed

* Increase number of records retained for 'site_info' table 1 -> 1000

### Known Issues

* Column has duplicated suffix ('CO2_ppm_Avg_Avg') in 'stats5/stats30' tables

### Enhancements

* New durable settings file used to track activation flags for Los Gatos N2O/CO,
  Picarro CO2/CH4, and new Decagon NDVI/PRI sensors, as well as scaling offsets
  and multipliers for Los Gatos & Picarro signals
* Support for new Decagon NDVI/PRI light sensors

### Wiring Changes

* Remove Decagon 6-band radiometers from C5/G/12V
* Add Decagon NDVI/PRI sensors to C5/G/12V

### Data Table Changes

* Removed tables:
    * stats5_6rad/stats30_6rad
    * tsdata_lgrn2oco/tsdata_picco2ch4
* New tables:
    * tsdata_extra 
        * output at 10 Hz
        * contains both LGR N2O/CO/H2O and Picarro CO2/CH4/H2O; if either is 
          missing, associated columns will be null values ("NAN")
        * units for all columns are "scale-dependent"
    * stats5_ui/stats30_ui
        * output on 5- and 30-min intervals
        * contains 9 columns (averages of ndvi/pri|up/down and total # of calls
          to tables)
    * extra_info
        * output whenever settings change, up to 1000 records
        * tracks presence of Decagon NDVI/PRI, LGR N2O/CO and Picarro CO2/CH4
          sensors, also multipliers/offsets for LGR & Picarro
    * diagnostics
        * output on 5-min intervals
        * contains number of total scans, skipped scans and watchdog errors
* Changes to 'stats5/stats30'
    * Add soil heat flux and plate sensitivity (4 columns total), after soil
      moisture probes
* Changes to 'site_daily'
    * Modify size from auto-allocate -> 60
    * Add min/max battery voltage and min/max temperature from T/RH probe
* Changes to 'site_info'
    * FIX: increase number of records retained 1 -> 1000
    * Remove columns tracking presence of Decagon 6-band radiometers, LGR 
      N2O/CO and Picarro CO2/CH4

### Other Changes

* Return fast & slow scan buffers 2 -> 1 min
* Modify soil heat flux plate calibration interval 3 -> 6 hours
* Acquire data from GPS receiver & soil moisture probes within soil heat flux
  plate scan (1/5 Hz) instead of 'slow' scan (1 Hz)
* New menu "Sensor Setup" contains options to enable/disable Decagon NDVI/PRI,
  LGR N2O/CO, and Picarro CO2/CH4 sensors
* Internally, fieldnames are promoted upwards to become variable names
* Restore copyright notice


20130416_MMTN
-------------

This version has the Los Gatos analyzer channels enabled; it expects analog 
voltage signals for N2O, CO and H2O.

### Known Issues

* In 'stats5/stats30' data tables, `rslt_wnd_dir` is not adjusted for sonic's
  orientation; add the sonic azimuth value to recorded WD for correct WD
    * HOW FAR BACK DOES THIS GO
    * since now recording `rslt_wnd_dir` instead of saving `wnd_dir_compass` as
      that name, the lack of compensation is important, also it means previous
      program versions are unaffected

### Enhancements

* Add support H2O signal from Los Gatos (LGR) N2O/CO analyzer
    * Analog voltage input on DIFF 10 
    * Units are mV, must be post-scaled to engineering units

### Data Table Changes

* Enable 'tsdata_lgrn2oco' table
* Increase data type size of Obukhov length `L` from FP2 -> IEEE4

### Other Changes

* **Activate** the Los Gatos N2O/CO analyzer inputs
    * Current implentation requires program operate in `SequentialMode` instead
      of `PipeLineMode`
* Increase flux (high-freq) scan and met (slow) scan buffers 1 -> 2 minutes
* Revert secondary, slow scan interval 3 -> 1 sec
* Simplify processing of resultant wind direction 
    * Introduces error mentioned under Known Issues
    * Calculate directly into geo-compass (left-handed) instead of sensor 
      (right-handed) coordinates
* Soil heat flux related
    * Comment out data tables, measurement code & processing 
    * Add framework for automatic activation based on logger serial number
    * Decrease scan frequency from 4 -> 5 seconds
    * Set sensitivity values to 0 if sensors are deactivated


20130123_CFNT
-------------

### Issues Fixed

* Change some variables' units:
    * `rho_d_mean_hmp`: kg/m^3 -> g/m^3  
      *Was introduced in version tagged 20120627_CFCT but never saved to data 
      tables*
    * `nmbr_clock_change`: samples -> occurrences  
      *Represents number of clock changes*

### Data Table Changes

* Re-activated globally: **stats5_hfp/stats30_hfp**
* Within **site_daily**, change units of nmbr_clock_change (see above)

### Other Changes

* Modify some scan intervals:
    * secondary, slow sensor scan: 1 -> 3 sec
    * heat flux plate scan: 4 -> 5 sec


20120827_XXXX
-------------

### Data Table Changes

* Deactivated globally: **stats5_hfp/stats30_hfp**
* Split **tsdata_gases** into **tsdata_lgrn2oco** and **tsdata_picco2ch4**

### Other Changes

* Globally deactivate soil heat flux plate


20120824_LIND
-------------

### Data Table Changes

* Within **stats5/stats30**, change dielectric value column names and units
    * soil_5TM_ID*_epsilon -> soil_5TM_ID*_E
    * dimensionless -> dimless
* Add columns to **stats5_hfp/stats30_hfp**: hfp1_samples_Tot, hfp2_samples_Tot,
  tblcalls_Tot
* Add columns to **stats5_6rad/stats30_6rad**: tblcalls_Tot

### Other Changes

* Move soil heat flux plate to an independent secondary scan at 1/4 Hz
* Reduce other slow scan buffer from 2 -> 1 min


20120810_LIND
-------------

### Enhancements

* Add support for measuring H2O from Picarro CH4/CO2/H2O analyzer on DIFF 13
* Filter null values ("NAN") from data recorded to 'stats5_6rad/stats30_6rad'
* Auxilary sensors 6-band radiometer (Decagon) and soil heat flux plate
  (Huskeflux) are now set on/off automatically based on site (logger S/N)

### Wiring Changes

* Optional Los Gatos Analyzer N2O/CO move from DF 10/11 to DF 8/9 respectively
* RESERVED FUTURE Optional Los Gatos Analyzer H2O input on DF 10
* Optional Picarro Analyzer CO2/CH4 move from DF 12/13 to 11/12 respectively
* NEW Optional Picarro Analyser H2O input on DF 13

### Data Table Changes

* Remove data tables: 
    * tsdata_n2o_co
    * stats5_n2o_co
    * stats30_n2o_co
    * tsdata_co2_ch4
    * stats5_co2_ch4
    * stats30_co2_ch4
* Create data table: tsdata_gases
    * Records 10 Hz time series of N2O, CO from LGR analyzer & CO2, CH4, H2O 
      from Picarro analyzer
* Move columns from **stats5_soil/stats30_soil** to **stats5/stats30**: 
  dielectric value, temperature, and volumetric water content from each of the 
  five soil moisture probes
* Rename data tables:
    * stats5_soil -> stats5_hfp
    * stats30_soil -> stats30_hfp
* Remove column from **site_info** table: SENSOR_DEC_5TM
* Rename columns in **site_info** table:
    * SENSOR_DEC_6RAD -> Dec_6rad_installed
    * SENSOR_LGR_N2OCO -> LGR_n2o_co_installed
    * SENSOR_PIC_CO2CH4 -> Pic_co2_ch4_installed
    * SENSOR_HFP01SC -> hfp_installed

* Units changes
    * irga_uptime: ratio -> unity

### Other Changes

* Processing for 5- and 30-min data tables is substantially simplified
    * Processing based on 'min_uptime' values is removed entirely
    * Data tables are consolidated and inter-scan triggers used instead
    * No stats created for auxilary trace gas analyzers (LGR, Picarro)


20120727_LIND
-------------

> **This version is a stub branch of 20120220_CFNT**

### Data Table Changes

* Increase size of 'site_info' table 1 -> 20 to allow to unintended restarts

### Other Changes

* Update auxilary sensors to match site
    * Deactivate Decagon 6-band radiometers    
    * Deactivate Los Gatos N2O/CO
    * Activate soil heat flux plate
* Add duplicate statements to end soil heat flux calibration interval


20120720_CFNT
-------------

* Activate Los Gatos N2O/CO analyzer


20120720_CFCT
-------------

* Activate Decagon 6-band radiometers


20120720_MMTN
-------------

* Revert some soil heat flux plate calibration routine schedule changes
    * Increase routine interval 2 -> 3 hr
    * Increase start time into interval delay 10 -> 120 sec
    * Increase total routine runtime to 380 sec
* Increase slow scan buffer 1 -> 2 min


20120711_MMTN
-------------

### Other Changes

* NEW monitoring site: Moscow Mountain Road (MMTN)
    * Sensor sensitivity values, sonic orientation, etc added
    * Soil heat flux plate (active at LIND) deactivated
* Slow scan buffer increased from 3 -> 60 sec


20120705_LIND
-------------

### Issues Fixed

* Fix problem preventing soil heat flux plate data from being recorded if soil
  moisture probes were not activated

### Data Table Changes

* In table site_info, change data type of soil heat flux plate sensitivity
  from FP2 to IEEE4 

### Other Changes

* Modify schedule of self-calibration routine of soil heat flux plates
    * Increase routine interval 3->2 hr
    * Reduce starting time into interval 60 -> 10 sec
    * Reduce heat-on time after start time 180 -> 20 sec
    * Change duration from heat-on+180s to start-time+190s


20120628_CFNT
-------------

### Issues Fixed

* Record null values ("NAN") instead of 0 if soil heat flux plates are not used

### Other changes

* Activate Los Gatos N2O/CO analyzer


20120627_CFCT
-------------

This version represents a lot of changes which means this entry is more likely
than others to be less than comprehensive.

### Enhancements

* Site-specific sensitivity values for certain sensors are now automatically
  selected using datalogger's serial number when program is compiled.
* Support for new auxilary sensors (not enabled by default)
    * Los Gatos N2O/CO analyzer, 2 analog voltage inputs, high-freq. sampling
    * Picarro CH4/CO2 analyzer, 2 analog voltage inputs, high-freq. sampling
    * Decagon soil moisture probes (5TM), 5 sensors
    * Huskeflux soil heat flux plates, 2 sensors

### Known Issues

* Disable flag for Picarro CO2/CH4 analyzer only checked for CO2=NAN, checked
  twice

### Wiring Changes

Consult the reference sheet `wiring_details.ods` for details.

* Cup & vane wind direction signal: SE 11 -> SE 1
* NEW Picarro Fast CO2/CH4/H2O analyzer
    * CO2: DIFF 12
    * CH4: DIFF 13
* SDI sensors including Decagon soil moisture probes and Decagon 6-band 
  radiometers: C5, 12V, G
* Soil heat flux plates (used in pairs) on: DF 6/7, SE 27/28, VX1, SW12-1, G

### Data Table Changes

* NEW data tables
    * **site_info**
        * Includes sonic_azimuth, RunSig, and ProgSig, moved from **site_daily**
        * Also contains site-specific metadata like clock offset from UTC,
          sensor sensitivity values, and flags indicating presence of auxilary
          instruments
    * **stats5_soil/stats30_soil**
        * For each probe measure: **epsilon**, dielectric permittivity;
          **T**, soil temperature; and **VWC**, volumetric water content calculated
          using the Topp equation
        * If soil heat flux plates are present, then soil heat flux and current
          sensitivity values
    * **tsdata_co2_ch4**, **stats5_co2_ch4**, **stats30_co2_ch4**
        * Analagous to tsdata_n2o_co, stats5_n2o_co, stats30_n2o_co
        * 5- and 30-min tables have mean and standard deviation of each scalar
        * Has "uptime" value too, which is # of non-NAN values over # scans

### Other Changes

* Remove base sensor set-related code from conditional compilation blocks
* Remove code related to sensors not deployed at any REACCH site
* Revise cup & vane WS sensor multiplier/offset: 0.799/0.2811 -> 0.7989/0.28
* Add conditional so wind-speed adjustment is only applied when WS > 5 m/s
    * If no refererence is found for this, it may be tagged a 'known issue'

### References

* Decagon Devices. *Dr. Topp.* <http://www.decagon.com/micro/dr-topp/>.
    * Topp, G.C., J.L. David, and A.P. Annan 1980. Electromagnetic, 
      Determination of Soil Water Content: Measurement in Coaxial Transmission 
      Lines. Water Resources Research 16:3. p. 574-582.


20120601_LIND
-------------

### Data Table Changes

* Drop data tables tsdata_n2o_co, stats5_n2o_co and stats30_n2o_co since 
  Los Gatos N2O/CO analyzer completely disabled

### Other Changes

* Comment out Los Gatos N2O/CO analyzer code


20120504_LIND
-------------

### Issues Fixed

* Corrected net radiometer and PAR sensor sensitivity values

### Data Table Changes

* Rename data tables
    * tsdata_extra -> tsdata_n2o_co
    * stats5_extra -> stats5_n2o_co
    * stats30_extra -> stats30_n2o_co
* Changed units within tsdata_n2o_co table
    * lgr_n2o: ppm, dMR -> ppm
    * lgr_co: ppm, dMR -> ppm
* Remove covariance terms from stats5_n2o_co and stats30_n2o_co tables


20120427_CFNT
-------------

### Data Table Changes

* NEW data tables **stats5_6rad** and **stats30_6rad** for Decagon radiometers

### Other Changes

* Add support for Decagon 6-band radiometers
    * Swapped sensor SDI addresses: up-facing is now 2, down-facing is 0
* Disable Los Gatos N2O/CO analyzer
* Verify net rad, PAR sensor sensitivity values are correct for CFNT site


20120420_LIND
-------------

### Known Issues

* Sensitivity values used for net radiometer and PAR sensor were incorrect,
  actually for CFNT sensor set, not LIND sensor set

### Data Table Changes

* New data tables
    * tsdata_extra: 10 Hz samples of N2O & CO
    * stats5_extra/stats30_extra: summary stats on 5- & 30-min intervals
        * Includes covariance between vertical wind speed & species conc but
          delay through sampling tube is not compensated for, therefore
          covariance values should be ignored

### Other Changes

* Add support for Los Gatos N2O/CO analyzer
    * Analog voltage input: N2O/DF 10, CO/DF 11
* Reduce analog input voltage measurement integration time: _60Hz -> 250


20120330_CFNT
-------------

Incorporate changes from 20120323_LIND


20120323_LIND
-------------

Manually incorporates changes from 20120316_CFNT

### Issues Fixed

* Add missing type code suffix "_Med" to `latitude` and `longitude`

### Data Table Changes

* In daily data table, 
    * Add missing type code suffix "_Med" to `latitude` and `longitude`
    * Remove average latitude, longitude, and magnetic_variation
    * Add median altitude (in addition to mean) since it presents more
      variance apparently


20120316_CFNT
-------------

### Data Table Changes

* In 5- & 30-min data tables rename `Met1_wnd_dir` to `Met1_rslt_wnd_dir`
* In daily table
    * Change units for latitude/longitude from 'decimal degrees N/E' to
      'decDegreesN/E' respectively
    * Add two columns `RunSig` and `ProgSig`

### Other Changes

* Specified sensitivity values for net radiometer, PAR sensor at CFNT site


20120309_LIND
-------------

This vesion was manually (imperfectly) merged against **20120215_CFNT**.

### Issues Fixed

* Removed site code prefix from data tables
* Correct data table reference; before this fix, since 20120215_CFNT, values
  from the T/RH probe recorded in 30-min data table were mistakenly duplicates
  of most recent 5-min period values. 
* Add missing units to CO2/H2O signal strength values in table 'tsdata'
* Remove slowsequence disable flags from daily table to restore output

### Data Tables

* Renamed data tables:
    * CFNT_stats5 -> stats5
    * CFNT_stats30 -> stats30
    * CFNT_site_daily -> site_daily
    * CFNT_tsdata -> tsdata 
* Changed units for variables:
    * `latitude_a`: degrees -> degreesN
    * `latitude_b`: minutes -> minutesN
    * `longitude_a`: degrees -> degreesE
    * `longitude_b`: minutes -> minutesE
    * `magnetic_variation`: unitless -> degreesEofN
    * `diag_sonic`: arb -> bitmap
    * `diag_irga`: arb -> bitmap
* Modify 5- & 30-min data tables:
    * Remove columns: Tc_Std, CO2_ppm_Std, H2O_g_kg_Std, hmp_uptime, Met1_uptime
    * Rename `wnd_dir_compass` to `rslt_wnd_dir` and move upward one column
* Add median values to daily table of GPS-related data
    * `latitude`: decimal_degrees_N
    * `longitude`: decimal_degrees_E
    * `magnetic_variation_Med`: degreesEofN

### Other Changes

* Revert many tables & variables back to hidden
* Simplify significantly the evaluation of sonic anemometer diagnostic word
* Also simplify the evaluation of IRGA diagnostic word
* Exclude negative values from PAR sensor


20120309_CFNT
-------------

> **This version is a stub branch of 20120224_LIND**

### Issues Fixed

* Correct data table reference; before this fix, since 20120215_CFNT, values
  from the T/RH probe recorded in 30-min data table were mistakenly duplicates
  of most recent 5-min period values. 


20120224_LIND
-------------

This version diverged from an earlier, unretained draft of **20120215_CFNT**. 

### Known Issues

* New `sonic_uptime` name incorrectly attached to `wnd_dir_compass` values
  while `wnd_dir_compass` name incorrectly reflects `sonic_uptime` values
* Implementation of `*_uptime` variables may have been flawed, always 
  indicating "1"

### Issues Fixed

* Update constant `SITE_PRESS` to 93.5 kPa (based on Dec 2011 - Feb 2012)
* Fix cause of `T_hmp` being 0 and `RH_hmp_Avg` being "NAN",
  which was a missing `GetRecord` statement
* In some instances, standard deviation of wind direction is reported zero, or
  site azimuth is recorded as wind direction because period lacked data and
  mean wind direction was reported zero. To resolve both, new value 
  `sonic_uptime` tracks ratio (0-1) of good sonic records out of queries; when
  value < 0.5 then null values ("NAN") are recorded for wind stats
* Use an `irga_uptime` analagous to sonic_uptime to set `Xc`/`Xv` to null
  value ("NAN") when irga_uptime < 0.5

### Data Table Changes

* Units are changed for several columns:
    * diag_sonic: arb -> bitmap
    * diag_irga: arb -> bitmap
    * CO2_sig_strgth: arb -> unity
    * H2O_sig_strgth: arb -> unity
* Modify both 5- and 30-min tables by
    * Adding columns: sonic_uptime, CO2_ppm_Std, H2O_g_kg_Avg, H2O_g_kg_Std,
      amb_tmpr_Avg, irga_samples_Tot, irga_uptime, e_hmp_Avg, e_sat_hmp_Avg,
      hmp_uptime, Met1_uptime

### Other Changes

* Updated calibration constants to reflect LIND-specific sensors
    * net radiometer (NR-Lite2): 12.6
    * PAR sensor (LI190SB): 6.84
* Modify multiplier used to value specified in user manual (0.799 -> 0.7989)
* Redefine several variables as Public to facilitate troubleshooting
* Modify behavior for cup & vane measurement QC
    * Change `If WS=0.2811 Then WS=0` to `If WS<=0.2811 Then WS=NAN`
    * Change `If WD>=360 Then WD=0` to `If WD>=360 OR WD<0 Then WD=NAN`


20120215_CFNT
-------------

### Issues Fixed

* Update constant `SITE_PRESS` to 93.5 kPa (based on Dec 2011 - Feb 2012)
* Fix cause of `T_hmp` being 0 and `RH_hmp_Avg` being "NAN",
  which was a missing `GetRecord` statement
* In some instances, standard deviation of wind direction is reported zero, or
  site azimuth is recorded as wind direction because period lacked data and
  mean wind direction was reported zero. To resolve both, new value 
  `sonic_uptime` tracks ratio (0-1) of good sonic records out of queries; when
  value < 0.5 then null values ("NAN") are recorded for wind stats
* Use an `irga_uptime` analagous to sonic_uptime to set `Xc`/`Xv` to null
  value ("NAN") when irga_uptime < 0.5

### Data Table Changes

* Units are changed for several columns:
    * diag_sonic: arb -> bitmap
    * diag_irga: arb -> bitmap
    * CO2_sig_strgth: arb -> unity
    * H2O_sig_strgth: arb -> unity
* Change both "CFNT_stats5" and "CFNT_stats30" tables by
    * Adding columns: sonic_uptime, CO2_ppm_Avg, H2O_g_kg_Avg, amb_tmpr_Avg,
      irga_uptime, e_hmp_Avg, e_sat_hmp_Avg
    * Removing columns: Tc_Std, sonic_samples_Tot
* Simplify daily GPS-related data table by removing standard deviation values

### Other Changes

* Modify multiplier used to value specified in user manual (0.799 -> 0.7989)
* Redefine several variables as Public to facilitate troubleshooting
* Modify behavior for cup & vane measurement QC
    * Change `If WS=0.2811 Then WS=0` to `If WS<=0.2811 Then WS=NAN`
    * Change `If WD>=360 Then WD=0` to `If WD>=360 OR WD<0 Then WD=NAN`


20120210_CFNT
-------------

### Issues Fixed

* Change cup & vane wind statistic output type set from 0->2 to match the type
  set output using sonic anemometer data
* Use correct temperature when calculating Monin-Obukhov Length
* Add back-end required for correct 5-min data table calculations
* Remove erroreous mixing ratio values co2_mix_ratio and h2o_mix_ratio,
  use Xc and Xv instead, respectively

### Data Table Changes

* Rename data tables:
    * "CFNT_met_5min" to "CFNT_stats5"
    * "flux" to "CFNT_stats30"
    * "ts_data" to "CFNT_tsdata"
* NEW data table "CFNT_site_daily" with GPS-related data, on 24hr output
* Modify 10 Hz table by removing columns: co2_molar_density, h2o_molar_density
* Modify both 5- & 30-min summary table structure
    * Column order changes significantly, see `data_table_key.ods` for details
    * Remove columns: Hs, latitude_a, latitude_b, longitue_a, longitude_b, 
      magnetic_variation, altitude, max_clock_change, nmbr_clock_change
    * Add columns: tau, Xc as CO2_ppm_Avg      
    * Rename columns: Ts_stdev to Ts_Std, Tc_mean to Tc_Avg, 
      Tc_stdev to Tc_Std, Uz_stdev to Uz_Std, CO2_mean to CO2_mg_m3_Avg, 
      H2O_mean to H2O_g_m3_Avg, CO2_stdev to CO2_mg_m3_Std, 
      H2O_stdev to H2O_g_m3_Std, CO2_sig_srgth to CO2_signal_Avg,
      H2O_sig_strgth to H2O_signal_Avg, amb_press_mean to amb_press_Avg,
      T_hmp_mean to T_hmp_Avg, RH_hmp_mean to RH_hmp_Avg
    * Change data types of `Rn` and `Rn_meas` from IEEE4 to FP2
    * Explicitly exclude null values ("NAN") when evaluating PAR sensor,
      cup & vane, and rain tipping bucket data
* Further modify the 30-min table by 
    * Removing these columns:
        * covariance values
        * ambient air density, rho_a_mean
        * component parts of flux calculations (raw covariance and both WPL terms)
        * diagnostic bits for IRGA (EC150)
        * some values from T/RH probe: e_hmp_mean, e_sat_hmp_mean, 
          H2O_hmp_mean, rho_a_mean_hmp
        * GPS-related values
    * And renaming these: l to L, par_totflx to PAR_totflx, par_flxdens to PAR_flxdens,
    * Additionally, change wind stat calculation type for cup & vane
        * mean horizontal wind speed: 034b_ws renamed to Met1_wnd_spd
        * unit vector mean wind direction: 034b_wd, removed
        * standard deviation of wind direction via Yamartino algorithm: 
          034b_stdwd, removed
        * mean wind vector magnitude: Met1_rslt_wnd_spd, added
        * resultant mean wind direction: Met1_wnd_dir, added
        * standard deviation of wind direction via Campbell Scientific
          algorithm: Met1_std_wnd_dir, added

### Other Changes

* Auto-allocate space on memory cards, effectively use all available space
* Disable the 'System Control' menu since instrument suite is static
* Save processing time by changing net rad. measurement from AutoRange to 20mV
* Disable both Los Gatos N2O/CO and Picarro CH4/CO2 analyzers
* Comment out superfluous code


20120204_CFNT
-------------

### Issues Fixed

* Add units "m" for meter to Monin-Obukhov Length (`L`)

### Known Issues

* New 5-min data table lacks back-end infrastructure to yield correct results

### Data Table Changes

* NEW data table "CFNT_met_5min" with select subset of values in the "flux"
  table on a 5-min instead of half-hour basis.
* Change variable names:
    * `l` to `L`
    * `par_mV` to `PAR_mV`
    * `par_flxdens` to `PAR_flxdens`
    * `par_totflx` to `PAR_totflx`


20111121_LIND
-------------

> **This is a stub branch of 20111101_CFNT**

This is the first release deployed at the Lind, WA site.

### Site-specific Changes 

* Update net radiometer sensitivity value
* Update PAR sensor sensitivity value


20111101_CFNT
-------------

**This release aggregates change made over three distinct deployed versions.
The intermediate work is unrecoverable.**

### Other Changes

* Add support for Los Gatos N2O/CO analyzer and Picarro CH4/CO2 analyzer but
  leave not enabled
* Remove support for ATI sonic anemometer, which had been disabled anyway
* Remove cruft associated with unused sensors


20111011_CFNT
-------------

**This release aggregates changes made over three distinct deployed versions.
The intermediate work is unrecoverable.**

### Issues fixed

* Change UTC offset from Central Standard (-6) to Pacific Standard (-8)
  *The precise time this change occurred has not been determined, though
  it may possibly be deduced from collected data.*
* Introduce 4 diagnostic flags for ATI sonic anemometer, one per data value
  Previous parsing method only retained final flag (`Ts` value)
* Temperature is now treated correctly in calculation of `Xc` and `Xv`

### Known Issues

* Variable `ati_azimuth` is declared twice and units are misspelled ("degress")
* Monin-Obukhov Length (`L`) is calculated using the variable `Tc_mean`, which
  is the mean "corrected" temperature from the CSAT3 sonic anemometer during
  the *last processed* half-hour period (30-60m prior), not the most recent
  half-hour period.
* Incorrect temperature is used when calculating `CO2_li_um_m`, `H2O_li_um_m`.
  *This mimics an earlier fix which, in this context, is an error.*

### Data Table Changes

* Fast time series: ts_data
    * Add inst. molar density and mixing ratio of CO2 & H2O
      (co2_molar_density, h2o_molar_density) 
      (present but commented out: CO2_mix_ratio, H2O_mix ratio)
    * Added but not enabled:
        * Instantaneous U/V/W/Ts from ATI sonic (atiUx, atiUy, atiUz, atiTs)
* Half-hour statistics: flux
    * Add Monin-Obukhov length (L) *See note under Known Issues*
    * Remove naive mean of WS for cup & vane (WS_ms)
    * Add field names and units to mean WS/WD, WD stdev for cup & vane
      (034b_ws, 034b_wd, 034b_stdwd)
    * Added but not enabled:
        * ATI sonic azimuth (ati_azimuth)
        * mean WS, mean WD, WD stdev, mean U/V/W/Ts for ATI sonic
          (ati_ws, ati_wd, ati_stdwd, atiUavg, atiVavg, atiWavg, atitmpavg)

### Other Changes

* ATI sonic anemometer
    * Do not open com port at start-up (no real change since not enabled)
    * Move input from COM1 to COM3
    * Calculate instanteous WS/WD for use in half-hour table stats
* Soil heat flux plates
    * Reduce number of soil heat flux plates from 4 -> 2
    * Add actual sensor-specific sensitivity values
* Cup & vane wind sensor
    * Change wind speed units from "meters/second" -> "m/s"


20110819_CFNT
-------------

* Initial version deployed
* Modified from original work by Campbell Scientific to also record data from
  Applied Technology Inc (ATI) sonic anemometer

### Known Issues

* Wrong time zone specified: Central Standard (-6) not Pacific Standard (-8)
* Only final ATI diagnostic word retained, first three are discarded 
* Temperature incorrectly subjected to unit conversion in calculation of `Xc`
  and `Xv`

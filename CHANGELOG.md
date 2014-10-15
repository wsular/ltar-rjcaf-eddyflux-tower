Change Log for GHG Monitoring Tower Program
===========================================

20120204_CFNT
-------------

### Issues Fixed

* Add units "m" for meter to Monin-Obukhov Length (`L`)

### Data Table Changes

* NEW data table "CFNT_met_5min" with select subset of values in the "flux"
  table on a 5-min instead of half-hour basis.
* Change variable names:
    * `l` to `L`
    * `par_mV` to `PAR_mV`
    * `par_flxdens` to `PAR_flxdens`
    * `par_totflx` to `PAR_totflx`


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

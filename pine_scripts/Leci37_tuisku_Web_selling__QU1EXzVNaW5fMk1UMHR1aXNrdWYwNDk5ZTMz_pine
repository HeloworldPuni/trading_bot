//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Triple_EMA
// ID_model: AMD_5Min_2MT0_f0499e33 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AMD_5Min_2MT0_f0499e33", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AMD_5Min_f0499e33(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, ema3, tema, ema2, ema12, ema13, ema1)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( Money_Flow_Ratio <= 0.15697 )
		if( Raw_Money_Flow <= 2.93522e+08 )
			if( tema <= 102.334 )
				if( ema12 <= -0.408462 )
					if( Negative_Money_Flow_Sum <= 6.1501e+08 )
						if( Money_Flow_Ratio <= 0.022019 )
							ret := -1.000000 // sell
						if( Money_Flow_Ratio > 0.022019 )
							if( Positive_Money_Flow_Sum <= 5.24469e+06 )
								ret := 0.000000
							if( Positive_Money_Flow_Sum > 5.24469e+06 )
								ret := 0.800000 // buy
					if( Negative_Money_Flow_Sum > 6.1501e+08 )
						if( ema2 <= 102.736 )
							if( Raw_Money_Flow <= 7.07286e+07 )
								ret := 0.800000 // buy
							if( Raw_Money_Flow > 7.07286e+07 )
								ret := 1.000000 // buy
						if( ema2 > 102.736 )
							ret := -0.333333
				if( ema12 > -0.408462 )
					if( Raw_Money_Flow <= 1.55032e+08 )
						if( Raw_Money_Flow <= 1.14929e+08 )
							if( ema3 <= 102.557 )
								if( Raw_Money_Flow <= 1.02348e+08 )
									ret := 0.016575
								if( Raw_Money_Flow > 1.02348e+08 )
									ret := -0.777778 // sell
							if( ema3 > 102.557 )
								if( ema13 <= -0.39523 )
									ret := 1.000000 // buy
								if( ema13 > -0.39523 )
									ret := 0.500000
						if( Raw_Money_Flow > 1.14929e+08 )
							if( tema <= 95.9011 )
								if( ema13 <= -0.362348 )
									ret := 0.250000
								if( ema13 > -0.362348 )
									ret := -0.250000
							if( tema > 95.9011 )
								if( MFI_High <= -77.0834 )
									ret := 1.000000 // buy
								if( MFI_High > -77.0834 )
									ret := 0.400000
					if( Raw_Money_Flow > 1.55032e+08 )
						if( Positive_Money_Flow_Sum <= 8.80724e+06 )
							if( Negative_Money_Flow <= 1.70332e+08 )
								ret := 0.750000 // buy
							if( Negative_Money_Flow > 1.70332e+08 )
								ret := -0.142857
						if( Positive_Money_Flow_Sum > 8.80724e+06 )
							if( Negative_Money_Flow_Sum <= 5.17344e+08 )
								if( ema1 <= 94.7151 )
									ret := -0.750000 // sell
								if( ema1 > 94.7151 )
									ret := -1.000000 // sell
							if( Negative_Money_Flow_Sum > 5.17344e+08 )
								ret := 0.200000
			if( tema > 102.334 )
				if( Positive_Money_Flow_Sum <= 2.67485e+07 )
					if( Raw_Money_Flow <= 2.10081e+08 )
						if( Negative_Money_Flow <= 1.34325e+08 )
							if( Negative_Money_Flow_Sum <= 1.25346e+09 )
								if( ema12 <= -0.221118 )
									ret := 0.164609
								if( ema12 > -0.221118 )
									ret := -0.043019
							if( Negative_Money_Flow_Sum > 1.25346e+09 )
								if( ema13 <= -0.767665 )
									ret := -1.000000 // sell
								if( ema13 > -0.767665 )
									ret := 0.000000
						if( Negative_Money_Flow > 1.34325e+08 )
							if( Raw_Money_Flow <= 1.66232e+08 )
								if( Negative_Money_Flow_Sum <= 1.08222e+09 )
									ret := -0.718447 // sell
								if( Negative_Money_Flow_Sum > 1.08222e+09 )
									ret := 0.600000
							if( Raw_Money_Flow > 1.66232e+08 )
								if( MFI_High <= -76.1965 )
									ret := 0.112903
								if( MFI_High > -76.1965 )
									ret := -0.575758
					if( Raw_Money_Flow > 2.10081e+08 )
						if( ema13 <= -1.73434 )
							if( tema <= 169.324 )
								ret := -1.000000 // sell
							if( tema > 169.324 )
								ret := 1.000000 // buy
						if( ema13 > -1.73434 )
							if( Negative_Money_Flow_Sum <= 2.75588e+08 )
								if( ema12 <= -0.054363 )
									ret := -0.631579
								if( ema12 > -0.054363 )
									ret := 0.600000
							if( Negative_Money_Flow_Sum > 2.75588e+08 )
								if( ema1 <= 157.575 )
									ret := 0.859649 // buy
								if( ema1 > 157.575 )
									ret := 0.604651
				if( Positive_Money_Flow_Sum > 2.67485e+07 )
					if( ema13 <= 0.018198 )
						if( ema12 <= -0.271723 )
							if( Negative_Money_Flow_Sum <= 3.38472e+09 )
								if( Positive_Money_Flow_Sum <= 1.81634e+08 )
									ret := -0.334076
								if( Positive_Money_Flow_Sum > 1.81634e+08 )
									ret := -0.101124
							if( Negative_Money_Flow_Sum > 3.38472e+09 )
								if( MFI_High <= -71.4725 )
									ret := 1.000000 // buy
								if( MFI_High > -71.4725 )
									ret := 0.250000
						if( ema12 > -0.271723 )
							if( ema1 <= 186.077 )
								if( Negative_Money_Flow_Sum <= 2.55578e+08 )
									ret := -0.900000 // sell
								if( Negative_Money_Flow_Sum > 2.55578e+08 )
									ret := 0.064516
							if( ema1 > 186.077 )
								if( Negative_Money_Flow <= 558509 )
									ret := -0.500000
								if( Negative_Money_Flow > 558509 )
									ret := -1.000000 // sell
					if( ema13 > 0.018198 )
						if( Raw_Money_Flow <= 6.80982e+07 )
							if( ema12 <= 0.15099 )
								ret := 0.000000
							if( ema12 > 0.15099 )
								ret := -0.250000
						if( Raw_Money_Flow > 6.80982e+07 )
							if( ema12 <= 0.151255 )
								if( Positive_Money_Flow_Sum <= 9.72889e+07 )
									ret := 1.000000 // buy
								if( Positive_Money_Flow_Sum > 9.72889e+07 )
									ret := 0.666667
							if( ema12 > 0.151255 )
								ret := 0.000000
		if( Raw_Money_Flow > 2.93522e+08 )
			if( Raw_Money_Flow <= 3.74992e+08 )
				if( ema1 <= 166.768 )
					if( MFI_High <= -71.4024 )
						if( Negative_Money_Flow_Sum <= 3.64277e+08 )
							if( Negative_Money_Flow_Sum <= 3.25735e+08 )
								if( MFI_High <= -74.6585 )
									ret := -1.000000 // sell
								if( MFI_High > -74.6585 )
									ret := 1.000000 // buy
							if( Negative_Money_Flow_Sum > 3.25735e+08 )
								ret := -1.000000 // sell
						if( Negative_Money_Flow_Sum > 3.64277e+08 )
							if( Negative_Money_Flow_Sum <= 1.15831e+09 )
								if( ema12 <= -0.233631 )
									ret := 0.714286 // buy
								if( ema12 > -0.233631 )
									ret := -1.000000 // sell
							if( Negative_Money_Flow_Sum > 1.15831e+09 )
								if( MFI <= 2.38641 )
									ret := -0.461538
								if( MFI > 2.38641 )
									ret := -0.947368 // sell
					if( MFI_High > -71.4024 )
						if( ema12 <= -0.147512 )
							if( ema2 <= 162.941 )
								if( Negative_Money_Flow_Sum <= 3.64699e+08 )
									ret := 1.000000 // buy
								if( Negative_Money_Flow_Sum > 3.64699e+08 )
									ret := 0.200000
							if( ema2 > 162.941 )
								ret := 1.000000 // buy
						if( ema12 > -0.147512 )
							ret := -1.000000 // sell
				if( ema1 > 166.768 )
					if( MFI_Low <= -19.3646 )
						ret := 0.750000 // buy
					if( MFI_Low > -19.3646 )
						if( ema12 <= -1.50802 )
							if( ema12 <= -1.66889 )
								ret := -0.800000 // sell
							if( ema12 > -1.66889 )
								ret := 0.400000
						if( ema12 > -1.50802 )
							if( ema12 <= -0.564317 )
								ret := -1.000000 // sell
							if( ema12 > -0.564317 )
								if( Positive_Money_Flow_Sum <= 4.43878e+07 )
									ret := -0.884615 // sell
								if( Positive_Money_Flow_Sum > 4.43878e+07 )
									ret := -0.500000
			if( Raw_Money_Flow > 3.74992e+08 )
				if( Negative_Money_Flow_Sum <= 8.61457e+08 )
					if( Typical_Price <= 166.528 )
						if( Negative_Money_Flow <= 5.48078e+08 )
							if( MFI_High <= -73.3641 )
								if( Raw_Money_Flow <= 4.28544e+08 )
									ret := 1.000000 // buy
								if( Raw_Money_Flow > 4.28544e+08 )
									ret := 0.625000
							if( MFI_High > -73.3641 )
								if( Negative_Money_Flow <= 4.38852e+08 )
									ret := -0.666667
								if( Negative_Money_Flow > 4.38852e+08 )
									ret := 1.000000 // buy
						if( Negative_Money_Flow > 5.48078e+08 )
							ret := -1.000000 // sell
					if( Typical_Price > 166.528 )
						if( Negative_Money_Flow <= 6.14913e+08 )
							if( Raw_Money_Flow <= 4.70583e+08 )
								ret := -1.000000 // sell
							if( Raw_Money_Flow > 4.70583e+08 )
								if( Negative_Money_Flow_Sum <= 6.6921e+08 )
									ret := -0.250000
								if( Negative_Money_Flow_Sum > 6.6921e+08 )
									ret := -1.000000 // sell
						if( Negative_Money_Flow > 6.14913e+08 )
							if( MFI <= 8.56809 )
								ret := 1.000000 // buy
							if( MFI > 8.56809 )
								ret := -0.142857
				if( Negative_Money_Flow_Sum > 8.61457e+08 )
					if( ema2 <= 133.45 )
						if( Negative_Money_Flow <= 3.93167e+08 )
							ret := 0.333333
						if( Negative_Money_Flow > 3.93167e+08 )
							if( Raw_Money_Flow <= 5.43436e+08 )
								ret := -1.000000 // sell
							if( Raw_Money_Flow > 5.43436e+08 )
								ret := -0.333333
					if( ema2 > 133.45 )
						if( MFI_Low <= -16.7048 )
							ret := 0.142857
						if( MFI_Low > -16.7048 )
							if( ema13 <= -0.331398 )
								if( ema13 <= -1.12246 )
									ret := 0.777778 // buy
								if( ema13 > -1.12246 )
									ret := 1.000000 // buy
							if( ema13 > -0.331398 )
								if( tema <= 152.439 )
									ret := 0.250000
								if( tema > 152.439 )
									ret := 0.600000
	if( Money_Flow_Ratio > 0.15697 )
		if( ema3 <= 215.204 )
			if( Positive_Money_Flow_Sum <= 1.16924e+09 )
				if( Negative_Money_Flow_Sum <= 2.53235e+07 )
					if( tema <= 121.74 )
						if( ema12 <= 0.103403 )
							if( Positive_Money_Flow <= 2.2079e+06 )
								if( ema13 <= -0.412769 )
									ret := 0.224490
								if( ema13 > -0.412769 )
									ret := -0.009928
							if( Positive_Money_Flow > 2.2079e+06 )
								if( MFI_High <= -47.9536 )
									ret := -0.437500
								if( MFI_High > -47.9536 )
									ret := 0.230088
						if( ema12 > 0.103403 )
							if( Positive_Money_Flow_Sum <= 3.76585e+06 )
								if( Raw_Money_Flow <= 714056 )
									ret := -0.084367
								if( Raw_Money_Flow > 714056 )
									ret := 0.347826
							if( Positive_Money_Flow_Sum > 3.76585e+06 )
								if( MFI_Low <= 37.2716 )
									ret := 0.510989
								if( MFI_Low > 37.2716 )
									ret := 0.142857
					if( tema > 121.74 )
						if( Positive_Money_Flow <= 1.28937e+07 )
							if( Raw_Money_Flow <= 6.45329e+06 )
								if( tema <= 167.342 )
									ret := 0.119118
								if( tema > 167.342 )
									ret := 0.035758
							if( Raw_Money_Flow > 6.45329e+06 )
								if( Positive_Money_Flow_Sum <= 2.73254e+07 )
									ret := 0.178322
								if( Positive_Money_Flow_Sum > 2.73254e+07 )
									ret := 0.484252
						if( Positive_Money_Flow > 1.28937e+07 )
							if( Typical_Price <= 148.023 )
								if( Positive_Money_Flow <= 2.29198e+08 )
									ret := -0.100671
								if( Positive_Money_Flow > 2.29198e+08 )
									ret := 0.555556
							if( Typical_Price > 148.023 )
								if( Positive_Money_Flow_Sum <= 9.24748e+08 )
									ret := -0.392562
								if( Positive_Money_Flow_Sum > 9.24748e+08 )
									ret := 0.772727 // buy
				if( Negative_Money_Flow_Sum > 2.53235e+07 )
					if( Positive_Money_Flow_Sum <= 1.24908e+08 )
						if( Positive_Money_Flow <= 7.57577e+06 )
							if( MFI <= 69.4128 )
								if( Positive_Money_Flow_Sum <= 2.27199e+07 )
									ret := 0.046776
								if( Positive_Money_Flow_Sum > 2.27199e+07 )
									ret := -0.086939
							if( MFI > 69.4128 )
								if( ema12 <= 0.145996 )
									ret := -0.238095
								if( ema12 > 0.145996 )
									ret := 0.696429
						if( Positive_Money_Flow > 7.57577e+06 )
							if( Money_Flow_Ratio <= 0.43056 )
								if( Negative_Money_Flow_Sum <= 1.2449e+08 )
									ret := 0.806452 // buy
								if( Negative_Money_Flow_Sum > 1.2449e+08 )
									ret := -0.076087
							if( Money_Flow_Ratio > 0.43056 )
								if( MFI_Low <= 52.4836 )
									ret := -0.386417
								if( MFI_Low > 52.4836 )
									ret := 0.212121
					if( Positive_Money_Flow_Sum > 1.24908e+08 )
						if( Positive_Money_Flow_Sum <= 3.46544e+08 )
							if( ema13 <= 0.548897 )
								if( Positive_Money_Flow_Sum <= 3.32067e+08 )
									ret := 0.098151
								if( Positive_Money_Flow_Sum > 3.32067e+08 )
									ret := 0.280374
							if( ema13 > 0.548897 )
								if( Money_Flow_Ratio <= 2.64784 )
									ret := -0.071942
								if( Money_Flow_Ratio > 2.64784 )
									ret := -0.709677 // sell
						if( Positive_Money_Flow_Sum > 3.46544e+08 )
							if( ema13 <= 0.834552 )
								if( ema12 <= -1.54043 )
									ret := -0.546512
								if( ema12 > -1.54043 )
									ret := 0.009443
							if( ema13 > 0.834552 )
								if( ema1 <= 107.184 )
									ret := 0.634146
								if( ema1 > 107.184 )
									ret := 0.133966
			if( Positive_Money_Flow_Sum > 1.16924e+09 )
				if( ema13 <= -0.345765 )
					if( ema13 <= -2.53417 )
						if( Raw_Money_Flow <= 3.35592e+08 )
							if( ema12 <= -1.22139 )
								ret := -1.000000 // sell
							if( ema12 > -1.22139 )
								ret := -0.250000
						if( Raw_Money_Flow > 3.35592e+08 )
							if( tema <= 164.869 )
								if( Negative_Money_Flow_Sum <= 3.97019e+09 )
									ret := 0.250000
								if( Negative_Money_Flow_Sum > 3.97019e+09 )
									ret := 1.000000 // buy
							if( tema > 164.869 )
								if( ema12 <= -1.57619 )
									ret := 0.200000
								if( ema12 > -1.57619 )
									ret := -0.600000
					if( ema13 > -2.53417 )
						if( Positive_Money_Flow <= 1.79499e+08 )
							if( Positive_Money_Flow_Sum <= 1.28766e+09 )
								if( MFI_High <= -40.6591 )
									ret := 0.161290
								if( MFI_High > -40.6591 )
									ret := 0.752809 // buy
							if( Positive_Money_Flow_Sum > 1.28766e+09 )
								if( Negative_Money_Flow_Sum <= 1.4514e+09 )
									ret := -0.277778
								if( Negative_Money_Flow_Sum > 1.4514e+09 )
									ret := 0.289256
						if( Positive_Money_Flow > 1.79499e+08 )
							if( Positive_Money_Flow_Sum <= 2.56799e+09 )
								if( ema13 <= -1.35051 )
									ret := 0.450000
								if( ema13 > -1.35051 )
									ret := 0.769697 // buy
							if( Positive_Money_Flow_Sum > 2.56799e+09 )
								if( Positive_Money_Flow <= 2.51735e+08 )
									ret := 1.000000 // buy
								if( Positive_Money_Flow > 2.51735e+08 )
									ret := -0.555556
				if( ema13 > -0.345765 )
					if( Negative_Money_Flow_Sum <= 1.14522e+09 )
						if( MFI_High <= -17.0715 )
							if( Positive_Money_Flow <= 1.53388e+08 )
								if( Typical_Price <= 110.519 )
									ret := -0.156250
								if( Typical_Price > 110.519 )
									ret := 0.397059
							if( Positive_Money_Flow > 1.53388e+08 )
								if( ema1 <= 184.527 )
									ret := 0.149533
								if( ema1 > 184.527 )
									ret := -0.547619
						if( MFI_High > -17.0715 )
							if( Typical_Price <= 107.912 )
								if( Negative_Money_Flow_Sum <= 5.259e+08 )
									ret := 0.650273
								if( Negative_Money_Flow_Sum > 5.259e+08 )
									ret := -0.338983
							if( Typical_Price > 107.912 )
								if( Positive_Money_Flow_Sum <= 2.97651e+09 )
									ret := 0.059091
								if( Positive_Money_Flow_Sum > 2.97651e+09 )
									ret := 0.466346
					if( Negative_Money_Flow_Sum > 1.14522e+09 )
						if( Positive_Money_Flow_Sum <= 3.88627e+09 )
							if( Negative_Money_Flow_Sum <= 2.20114e+09 )
								if( Positive_Money_Flow_Sum <= 3.47905e+09 )
									ret := -0.016310
								if( Positive_Money_Flow_Sum > 3.47905e+09 )
									ret := 0.677419
							if( Negative_Money_Flow_Sum > 2.20114e+09 )
								if( MFI_Low <= 15.1278 )
									ret := 0.750000 // buy
								if( MFI_Low > 15.1278 )
									ret := -0.505747
						if( Positive_Money_Flow_Sum > 3.88627e+09 )
							if( Typical_Price <= 180.961 )
								ret := 0.000000
							if( Typical_Price > 180.961 )
								if( tema <= 208.762 )
									ret := -1.000000 // sell
								if( tema > 208.762 )
									ret := -0.750000 // sell
		if( ema3 > 215.204 )
			if( Negative_Money_Flow <= 5.62341e+08 )
				ret := -1.000000 // sell
			if( Negative_Money_Flow > 5.62341e+08 )
				ret := -0.750000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Money_Flow_Index 
//@version=5
//indicator title="Money Flow Index (MFI)", shorttitle="MFI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)

// Input parameters
length_MFI = input.int(14, minval=1, title="MFI Length")

// Calculate the Typical Price
Typical_Price = (high + low + close) / 3

// Calculate Raw Money Flow
Raw_Money_Flow = Typical_Price * volume

// Calculate Positive and Negative Money Flow
Positive_Money_Flow = Raw_Money_Flow * (Typical_Price > Typical_Price[1] ? 1 : 0)
Negative_Money_Flow = Raw_Money_Flow * (Typical_Price < Typical_Price[1] ? 1 : 0)

// Sum of Positive and Negative Money Flow over the given length
Positive_Money_Flow_Sum = ta.sma(Positive_Money_Flow, length_MFI) * length_MFI
Negative_Money_Flow_Sum = ta.sma(Negative_Money_Flow, length_MFI) * length_MFI

// Calculate Money Flow Ratio
Money_Flow_Ratio = Positive_Money_Flow_Sum / Negative_Money_Flow_Sum

// Calculate MFI
MFI = 100 - (100 / (1 + Money_Flow_Ratio))

// Calculate MFI high and low bands
MFI_High = MFI - 80
MFI_Low = MFI - 20

// Plot the MFI
plot(MFI, color=color.blue, title="MFI")

// Plot the MFI high and low bands
hline(80, "MFI High", color=color.red, linestyle=hline.style_dashed)
hline(20, "MFI Low", color=color.green, linestyle=hline.style_dashed)
plot(MFI_High, color=color.red, title="MFI High Band")
plot(MFI_Low, color=color.green, title="MFI Low Band")


//CODE associated with the technical indicator L_Triple_EMA 
//@version=5
//indicator title="Triple EMA", shorttitle="TEMA", overlay=true, timeframe="", timeframe_gaps=true)
length_TEMA = input.int(9, minval=1)
ema1 = ta.ema(close, length_TEMA)
ema2 = ta.ema(ema1, length_TEMA)
ema3 = ta.ema(ema2, length_TEMA)
tema = 3 * (ema1 - ema2) + ema3
plot(tema, "TEMA", color=#2962FF)

ema12 = ema1 - ema2
ema13 = ema1 - ema3


// EXPLANATION OF THE STRATEGY
//The provided Pine Script implements a trading strategy that includes stop loss (SL) and multiple take profit (TP) levels,
//with an option to activate a trailing stop at the third TP level. Here's a detailed breakdown of its components and functionality:

//Variables Initialization:
var float stop = na
var float limit1 = na
var float limit2 = na

// Converts a percentage to points based on the average position price and the minimum tick size.
percent2points(percent) =>
    strategy.position_avg_price * percent / 100 / syminfo.mintick

// Stop Loss and Take Profit Inputs:
//Defines inputs for stop loss and three take profit levels in percentage terms.
sl = percent2points(input(2.92, title="stop loss %%"))
tp1 = percent2points(input(1.12, title="take profit 1 %%"))
tp2 = percent2points(input(2.31, title="take profit 2 %%"))
tp3 = percent2points(input(3.91, title="take profit 3 %%"))
activateTrailingOnThirdStep = input(false,title="activate trailing on third stage (tp3 is amount, tp2 is offset level)")
log.info("Stop Loss (sl):", sl," Take Profit 1 (tp1):", tp1, " Take Profit 2 (tp2):", tp2," Take Profit 3 (tp3):", tp3)

// Current Profit Calculation:
//Calculates the current profit in points based on the position size and price.
curProfitInPts() =>
    if strategy.position_size > 0
        (high - strategy.position_avg_price) / syminfo.mintick
    else if strategy.position_size < 0
        (strategy.position_avg_price - low) / syminfo.mintick
    else
        0
// Stop Loss and Profit Target Price Calculations:
//Determines the stop loss and profit target prices based on the position size and offset points.
calcStopLossPrice(OffsetPts) =>
    if strategy.position_size > 0
        strategy.position_avg_price - OffsetPts * syminfo.mintick
    else if strategy.position_size < 0
        strategy.position_avg_price + OffsetPts * syminfo.mintick
    else
        0
calcProfitTrgtPrice(OffsetPts) =>
    calcStopLossPrice(-OffsetPts)
// Current Stage Determination:
//Determines the current stage of the trade based on the profit points reached.
getCurrentStage() =>
    var stage = 0
    if strategy.position_size == 0
        stage := 0
    if stage == 0 and strategy.position_size != 0
        stage := 1
    else if stage == 1 and curProfitInPts() >= tp1
        stage := 2
    else if stage == 2 and curProfitInPts() >= tp2
        stage := 3
    stage
stopLevel = -1.
profitLevel = calcProfitTrgtPrice(tp3)

log.info("Stop Level:", stopLevel)
log.info("Profit Level:", profitLevel)
//This part of the strategy sets up exit conditions based on the current stage of the trade and uses the same exit ID "x" to modify the exit parameters dynamically.
//The exit parameters include stop loss, take profit, and comments for each stage.
// based on current stage set up exit
// note: we use same exit ids ("x") consciously, for MODIFY the exit's parameters
curStage = getCurrentStage()
float op_operation = decision_tree_0_AMD_5Min_f0499e33(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, ema3, tema, ema2, ema12, ema13, ema1)

log.info("Decision Tree Operation (op_operation):", op_operation)
if (op_operation <= 0)
    if curStage == 1
        stopLevel := calcStopLossPrice(sl)
        strategy.exit("x", loss = sl, profit = tp3, comment = "sl or tp3")
    else if curStage == 2
        stopLevel := calcStopLossPrice(0)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "breakeven or tp3")
    else if curStage == 3
        stopLevel := calcStopLossPrice(-tp1)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "tp1 or tp3")
    else
        strategy.cancel("x")


//SIGNAL MANAGE    User Adjustments and Risk Management
// The user can adjust the threshold values for op_operation to control the level of risk they are willing to take:
// Lower op_operation Threshold for Buy Signal (e.g., 0.5 instead of 0.55):
//     Effect: Generates more buy signals, increasing the frequency of trades. This is suitable for a user willing to take more risks and potentially capture more trading opportunities.
// Higher op_operation Threshold for Buy Signal (e.g., 0.8 instead of 0.55):
//     Effect: Generates fewer buy signals, reducing the frequency of trades. This is suitable for a user seeking to take fewer risks and only enter trades under more favorable conditions.
// Lower op_operation Threshold for Signal Closure (e.g., -0.8 instead of -0.9):
//     Effect: Closes positions less frequently, allowing trades more room to recover from temporary unfavorable conditions. This increases risk but can capture larger gains if the market reverses favorably.
// Higher op_operation Threshold for Signal Closure (e.g., -0.95 instead of -0.9):
//     Effect: Closes positions more frequently, exiting trades quickly at the first sign of unfavorable conditions. This decreases risk but may result in missed opportunities for recovery.
//Signal BUY
FIXED_DOLLAR_AMOUNT  = 10000
positionSize = FIXED_DOLLAR_AMOUNT / close
log.info("Position Size (in dollars $",FIXED_DOLLAR_AMOUNT,"):", positionSize)

if (op_operation >= 0.55)
    stop := close * 0.965
    limit1 := close * 1.03
    limit2 := close * 1.02
    strategy.entry("x", strategy.long, qty=positionSize, stop=stop, comment="in")
//Signal SELL
if (op_operation <= -0.9)
    strategy.close("x", comment = "under Le1")

// Impact on the Dataset
//Stop Loss (SL): Limits the maximum loss by exiting the position if the price moves against the trade by a specified percentage.
//Take Profit (TP1, TP2, TP3): Defines profit-taking levels to secure gains at different stages.
//Trailing Stop: Optionally activates a trailing stop at the third TP level to lock in profits while allowing for further gains if the price continues to move favorably.
//Position Entry and Exit: The strategy's buy and sell signals determine when to enter and exit positions, influencing the dataset by marking the points of trade execution and closure.
//Current Stage Tracking: Monitors the trade's progress through predefined stages, adjusting stop and profit levels accordingly.
//This strategy is designed to manage risk and maximize profits through a structured approach, incorporating multiple exit levels and dynamic adjustments based on market conditions. The dataset will reflect these actions, showing entries, exits, stop loss activations, and profit-taking events, providing valuable information for backtesting and performance analysis.
//Random forest AI offers significant advantages in trading, including the ability to handle large data sets, reduce overfitting and provide more robust predictions through the aggregation of multiple decision trees.

// NOTE: While the Tuisku team stands behind the quality and effectiveness of this trading strategy,
// PLEASE be aware that there is NO GUARANTEE of specific results or profits. TRADING INVOLVES SIGNIFICANT RISK, and it is important to use this strategy with careful consideration of your financial situation and risk tolerance.
// For further information and support, please contact us at Tuisku.eu.



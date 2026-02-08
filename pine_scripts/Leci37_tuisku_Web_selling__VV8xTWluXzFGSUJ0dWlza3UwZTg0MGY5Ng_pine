//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Fibonacci_Bollinger
// ID_model: U_1Min_1FIB_0e840f96 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_U_1Min_1FIB_0e840f96", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_U_1Min_0e840f96(lower_6, lower_3, basis_max, lower_1, upper_2, upper_6, upper_4, lower_2, basis_minus, upper_3, lower_5, upper_1, lower_4, basis, upper_5)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( upper_3 <= 16.3039 )
		if( basis_minus <= 0.113957 )
			if( lower_5 <= 15.7496 )
				if( lower_4 <= 15.1768 )
					if( basis <= 15.2437 )
						ret := -0.750000 // sell
					if( basis > 15.2437 )
						ret := -1.000000 // sell
				if( lower_4 > 15.1768 )
					if( basis_minus <= 0.108529 )
						if( upper_1 <= 15.5588 )
							if( upper_3 <= 15.5857 )
								ret := -1.000000 // sell
							if( upper_3 > 15.5857 )
								ret := -0.600000
						if( upper_1 > 15.5588 )
							if( lower_6 <= 15.4415 )
								if( upper_1 <= 15.5593 )
									ret := 0.000000
								if( upper_1 > 15.5593 )
									ret := 0.777778 // buy
							if( lower_6 > 15.4415 )
								if( basis_max <= -0.102739 )
									ret := -0.444444
								if( basis_max > -0.102739 )
									ret := 0.000000
					if( basis_minus > 0.108529 )
						if( lower_2 <= 15.6515 )
							if( upper_1 <= 15.7188 )
								if( lower_4 <= 15.4622 )
									ret := 0.277778
								if( lower_4 > 15.4622 )
									ret := 0.000000
							if( upper_1 > 15.7188 )
								ret := 0.750000 // buy
						if( lower_2 > 15.6515 )
							if( upper_2 <= 15.8026 )
								ret := 0.000000
							if( upper_2 > 15.8026 )
								ret := -0.250000
			if( lower_5 > 15.7496 )
				if( upper_1 <= 16.1099 )
					if( lower_6 <= 15.7295 )
						if( basis <= 15.8254 )
							ret := -1.000000 // sell
						if( basis > 15.8254 )
							ret := 0.000000
					if( lower_6 > 15.7295 )
						if( basis <= 15.8256 )
							ret := -0.750000 // sell
						if( basis > 15.8256 )
							ret := -1.000000 // sell
				if( upper_1 > 16.1099 )
					if( lower_1 <= 16.1753 )
						if( lower_3 <= 16.1518 )
							if( basis_max <= -0.092897 )
								if( basis_max <= -0.113661 )
									ret := -0.500000
								if( basis_max > -0.113661 )
									ret := 0.043478
							if( basis_max > -0.092897 )
								if( lower_2 <= 16.0662 )
									ret := 0.000000
								if( lower_2 > 16.0662 )
									ret := -0.541667
						if( lower_3 > 16.1518 )
							ret := 0.750000 // buy
					if( lower_1 > 16.1753 )
						if( basis_max <= -0.101001 )
							ret := -0.500000
						if( basis_max > -0.101001 )
							ret := -1.000000 // sell
		if( basis_minus > 0.113957 )
			if( upper_3 <= 16.2109 )
				if( upper_1 <= 14.2641 )
					if( upper_4 <= 14.8035 )
						if( upper_3 <= 14.3405 )
							if( upper_1 <= 13.9877 )
								if( lower_1 <= 13.5147 )
									ret := 0.150000
								if( lower_1 > 13.5147 )
									ret := 0.866667 // buy
							if( upper_1 > 13.9877 )
								if( lower_2 <= 13.8656 )
									ret := -0.222222
								if( lower_2 > 13.8656 )
									ret := 0.234450
						if( upper_3 > 14.3405 )
							if( basis_minus <= 0.392967 )
								if( lower_2 <= 14.04 )
									ret := 0.960000 // buy
								if( lower_2 > 14.04 )
									ret := 0.407407
							if( basis_minus > 0.392967 )
								if( basis_max <= -0.677967 )
									ret := 0.639344
								if( basis_max > -0.677967 )
									ret := -0.400000
					if( upper_4 > 14.8035 )
						if( basis_max <= -1.57539 )
							ret := 0.000000
						if( basis_max > -1.57539 )
							ret := -1.000000 // sell
				if( upper_1 > 14.2641 )
					if( basis_minus <= 0.95851 )
						if( upper_1 <= 14.3211 )
							if( upper_6 <= 14.4301 )
								if( upper_3 <= 14.339 )
									ret := -0.029703
								if( upper_3 > 14.339 )
									ret := 0.851852 // buy
							if( upper_6 > 14.4301 )
								if( lower_6 <= 13.8971 )
									ret := -0.230769
								if( lower_6 > 13.8971 )
									ret := -0.718519 // sell
						if( upper_1 > 14.3211 )
							if( upper_5 <= 14.5051 )
								if( upper_1 <= 14.3313 )
									ret := 0.157895
								if( upper_1 > 14.3313 )
									ret := 0.853333 // buy
							if( upper_5 > 14.5051 )
								if( lower_5 <= 16.0144 )
									ret := 0.091242
								if( lower_5 > 16.0144 )
									ret := 0.787234 // buy
					if( basis_minus > 0.95851 )
						if( upper_2 <= 14.8417 )
							if( upper_3 <= 14.7171 )
								ret := 0.600000
							if( upper_3 > 14.7171 )
								if( upper_1 <= 14.5975 )
									ret := -0.975610 // sell
								if( upper_1 > 14.5975 )
									ret := -0.764706 // sell
						if( upper_2 > 14.8417 )
							if( basis <= 15.5884 )
								if( upper_1 <= 14.7709 )
									ret := 0.361345
								if( upper_1 > 14.7709 )
									ret := -0.089286
							if( basis > 15.5884 )
								if( lower_1 <= 15.4048 )
									ret := -0.937500 // sell
								if( lower_1 > 15.4048 )
									ret := 0.250000
			if( upper_3 > 16.2109 )
				if( lower_3 <= 15.1597 )
					if( upper_3 <= 16.2826 )
						if( lower_6 <= 14.3843 )
							ret := 1.000000 // buy
						if( lower_6 > 14.3843 )
							if( upper_1 <= 15.9388 )
								ret := 0.500000
							if( upper_1 > 15.9388 )
								if( upper_4 <= 16.3539 )
									ret := 1.000000 // buy
								if( upper_4 > 16.3539 )
									ret := 0.750000 // buy
					if( upper_3 > 16.2826 )
						ret := 0.571429
				if( lower_3 > 15.1597 )
					if( upper_1 <= 15.9918 )
						if( lower_5 <= 14.875 )
							if( lower_6 <= 14.615 )
								ret := -1.000000 // sell
							if( lower_6 > 14.615 )
								ret := 0.500000
						if( lower_5 > 14.875 )
							if( lower_6 <= 14.6189 )
								ret := -0.500000
							if( lower_6 > 14.6189 )
								ret := -1.000000 // sell
					if( upper_1 > 15.9918 )
						if( lower_3 <= 15.9715 )
							if( lower_2 <= 15.9988 )
								if( upper_5 <= 16.3645 )
									ret := 0.509317
								if( upper_5 > 16.3645 )
									ret := 0.233236
							if( lower_2 > 15.9988 )
								if( basis_minus <= 0.335648 )
									ret := 0.901408 // buy
								if( basis_minus > 0.335648 )
									ret := 0.500000
						if( lower_3 > 15.9715 )
							if( lower_6 <= 16.0216 )
								if( lower_3 <= 16.0359 )
									ret := 0.126984
								if( lower_3 > 16.0359 )
									ret := -0.244186
							if( lower_6 > 16.0216 )
								if( lower_6 <= 16.0251 )
									ret := 0.852941 // buy
								if( lower_6 > 16.0251 )
									ret := 0.263473
	if( upper_3 > 16.3039 )
		if( basis <= 24.7032 )
			if( upper_3 <= 19.5163 )
				if( upper_6 <= 18.0485 )
					if( basis_minus <= 1.48917 )
						if( upper_6 <= 17.7553 )
							if( upper_1 <= 17.2116 )
								if( lower_1 <= 16.8683 )
									ret := 0.027546
								if( lower_1 > 16.8683 )
									ret := 0.143980
							if( upper_1 > 17.2116 )
								if( upper_4 <= 17.3472 )
									ret := -0.394659
								if( upper_4 > 17.3472 )
									ret := -0.041168
						if( upper_6 > 17.7553 )
							if( upper_6 <= 17.8161 )
								if( basis_max <= -0.968485 )
									ret := -0.500000
								if( basis_max > -0.968485 )
									ret := 0.458167
							if( upper_6 > 17.8161 )
								if( basis <= 16.8037 )
									ret := -0.385965
								if( basis > 16.8037 )
									ret := 0.097295
					if( basis_minus > 1.48917 )
						if( upper_5 <= 17.1574 )
							if( lower_1 <= 15.5167 )
								if( lower_3 <= 14.6323 )
									ret := 0.200000
								if( lower_3 > 14.6323 )
									ret := -0.714286 // sell
							if( lower_1 > 15.5167 )
								ret := 0.666667
						if( upper_5 > 17.1574 )
							if( upper_6 <= 17.9385 )
								if( lower_4 <= 15.1962 )
									ret := 0.730159 // buy
								if( lower_4 > 15.1962 )
									ret := 0.920635 // buy
							if( upper_6 > 17.9385 )
								if( lower_6 <= 14.6813 )
									ret := -0.857143 // sell
								if( lower_6 > 14.6813 )
									ret := 0.333333
				if( upper_6 > 18.0485 )
					if( lower_5 <= 16.4109 )
						if( lower_1 <= 15.1277 )
							ret := 1.000000 // buy
						if( lower_1 > 15.1277 )
							if( lower_4 <= 14.0488 )
								if( lower_5 <= 13.623 )
									ret := -0.764706 // sell
								if( lower_5 > 13.623 )
									ret := 1.000000 // buy
							if( lower_4 > 14.0488 )
								if( upper_5 <= 17.8266 )
									ret := -0.212766
								if( upper_5 > 17.8266 )
									ret := -0.592233
					if( lower_5 > 16.4109 )
						if( basis_minus <= 1.15286 )
							if( upper_5 <= 19.6071 )
								if( lower_4 <= 16.6442 )
									ret := 0.421569
								if( lower_4 > 16.6442 )
									ret := -0.045011
							if( upper_5 > 19.6071 )
								if( upper_4 <= 19.5514 )
									ret := 0.000000
								if( upper_4 > 19.5514 )
									ret := -0.725000 // sell
						if( basis_minus > 1.15286 )
							if( basis_max <= -2.19923 )
								if( upper_2 <= 19.2094 )
									ret := -0.952381 // sell
								if( upper_2 > 19.2094 )
									ret := -0.250000
							if( basis_max > -2.19923 )
								if( lower_4 <= 17.902 )
									ret := 0.781065 // buy
								if( lower_4 > 17.902 )
									ret := -0.062500
			if( upper_3 > 19.5163 )
				if( lower_4 <= 19.4176 )
					if( basis <= 19.6456 )
						if( upper_4 <= 20.0653 )
							if( lower_6 <= 19.035 )
								if( basis_minus <= 0.822827 )
									ret := 0.526316
								if( basis_minus > 0.822827 )
									ret := 0.050360
							if( lower_6 > 19.035 )
								if( upper_5 <= 19.9888 )
									ret := 0.073529
								if( upper_5 > 19.9888 )
									ret := -0.875000 // sell
						if( upper_4 > 20.0653 )
							if( basis_max <= -0.74104 )
								ret := -1.000000 // sell
							if( basis_max > -0.74104 )
								ret := 0.000000
					if( basis > 19.6456 )
						if( basis_minus <= 1.29299 )
							if( basis_minus <= 0.462414 )
								if( lower_3 <= 19.4334 )
									ret := 0.250000
								if( lower_3 > 19.4334 )
									ret := 0.000000
							if( basis_minus > 0.462414 )
								if( lower_6 <= 18.8945 )
									ret := -0.250000
								if( lower_6 > 18.8945 )
									ret := 0.686099
						if( basis_minus > 1.29299 )
							if( basis_max <= -1.29609 )
								ret := -0.750000 // sell
							if( basis_max > -1.29609 )
								ret := -0.285714
				if( lower_4 > 19.4176 )
					if( upper_5 <= 20.3976 )
						if( lower_3 <= 19.8225 )
							if( lower_3 <= 19.8085 )
								if( lower_5 <= 19.7297 )
									ret := -0.090439
								if( lower_5 > 19.7297 )
									ret := -0.806452 // sell
							if( lower_3 > 19.8085 )
								if( lower_2 <= 19.8543 )
									ret := 0.729167 // buy
								if( lower_2 > 19.8543 )
									ret := -0.200000
						if( lower_3 > 19.8225 )
							if( upper_4 <= 20.1895 )
								if( upper_5 <= 20.2267 )
									ret := -0.535714
								if( upper_5 > 20.2267 )
									ret := -0.870968 // sell
							if( upper_4 > 20.1895 )
								if( lower_6 <= 19.8645 )
									ret := -0.155556
								if( lower_6 > 19.8645 )
									ret := -1.000000 // sell
					if( upper_5 > 20.3976 )
						if( upper_6 <= 21.3085 )
							if( upper_5 <= 21.1647 )
								if( lower_5 <= 19.9649 )
									ret := 0.258407
								if( lower_5 > 19.9649 )
									ret := 0.079082
							if( upper_5 > 21.1647 )
								if( upper_5 <= 21.1669 )
									ret := 0.939394 // buy
								if( upper_5 > 21.1669 )
									ret := 0.491713
						if( upper_6 > 21.3085 )
							if( upper_3 <= 21.0425 )
								if( upper_2 <= 20.9699 )
									ret := -0.162730
								if( upper_2 > 20.9699 )
									ret := -0.842105 // sell
							if( upper_3 > 21.0425 )
								if( upper_3 <= 21.1068 )
									ret := 0.336493
								if( upper_3 > 21.1068 )
									ret := 0.045430
		if( basis > 24.7032 )
			if( lower_4 <= 24.2498 )
				if( upper_1 <= 25.0818 )
					if( lower_4 <= 24.0184 )
						if( lower_4 <= 23.8909 )
							if( upper_5 <= 25.7929 )
								if( basis_max <= -1.394 )
									ret := 0.000000
								if( basis_max > -1.394 )
									ret := -0.750000 // sell
							if( upper_5 > 25.7929 )
								if( upper_2 <= 25.3114 )
									ret := -1.000000 // sell
								if( upper_2 > 25.3114 )
									ret := -0.800000 // sell
						if( lower_4 > 23.8909 )
							if( lower_3 <= 24.1472 )
								ret := 0.750000 // buy
							if( lower_3 > 24.1472 )
								ret := -0.500000
					if( lower_4 > 24.0184 )
						if( upper_2 <= 25.1985 )
							if( lower_5 <= 23.8744 )
								if( lower_6 <= 23.5867 )
									ret := -0.894737 // sell
								if( lower_6 > 23.5867 )
									ret := -1.000000 // sell
							if( lower_5 > 23.8744 )
								if( basis <= 24.7583 )
									ret := 0.000000
								if( basis > 24.7583 )
									ret := -0.900000 // sell
						if( upper_2 > 25.1985 )
							ret := -0.250000
				if( upper_1 > 25.0818 )
					if( upper_4 <= 25.6402 )
						if( basis <= 24.7855 )
							ret := 0.000000
						if( basis > 24.7855 )
							ret := 1.000000 // buy
					if( upper_4 > 25.6402 )
						if( upper_5 <= 25.8316 )
							ret := -0.666667
						if( upper_5 > 25.8316 )
							if( upper_5 <= 25.8341 )
								ret := 0.428571
							if( upper_5 > 25.8341 )
								if( lower_6 <= 23.5163 )
									ret := -0.250000
								if( lower_6 > 23.5163 )
									ret := -0.500000
			if( lower_4 > 24.2498 )
				if( lower_1 <= 24.5801 )
					if( basis <= 24.7397 )
						if( lower_2 <= 24.4803 )
							if( lower_1 <= 24.5568 )
								ret := 0.750000 // buy
							if( lower_1 > 24.5568 )
								ret := 1.000000 // buy
						if( lower_2 > 24.4803 )
							ret := 0.400000
					if( basis > 24.7397 )
						if( basis_max <= -0.815639 )
							ret := 0.000000
						if( basis_max > -0.815639 )
							if( upper_1 <= 24.954 )
								if( lower_2 <= 24.4723 )
									ret := 0.181818
								if( lower_2 > 24.4723 )
									ret := 0.500000
							if( upper_1 > 24.954 )
								if( lower_3 <= 24.3628 )
									ret := 1.000000 // buy
								if( lower_3 > 24.3628 )
									ret := 0.750000 // buy
				if( lower_1 > 24.5801 )
					if( upper_1 <= 24.9428 )
						if( upper_2 <= 24.9969 )
							if( lower_4 <= 24.4044 )
								if( lower_3 <= 24.4625 )
									ret := 0.272727
								if( lower_3 > 24.4625 )
									ret := 0.000000
							if( lower_4 > 24.4044 )
								if( lower_2 <= 24.5308 )
									ret := -0.692308
								if( lower_2 > 24.5308 )
									ret := -0.055556
						if( upper_2 > 24.9969 )
							if( basis <= 24.7489 )
								ret := 0.000000
							if( basis > 24.7489 )
								if( lower_5 <= 24.4827 )
									ret := -0.957447 // sell
								if( lower_5 > 24.4827 )
									ret := -0.571429
					if( upper_1 > 24.9428 )
						if( upper_6 <= 25.7291 )
							if( upper_4 <= 25.0734 )
								if( upper_4 <= 25.0668 )
									ret := -0.140351
								if( upper_4 > 25.0668 )
									ret := -0.878049 // sell
							if( upper_4 > 25.0734 )
								if( upper_1 <= 24.992 )
									ret := 0.215139
								if( upper_1 > 24.992 )
									ret := -0.011790
						if( upper_6 > 25.7291 )
							if( lower_3 <= 24.5487 )
								if( upper_5 <= 25.8128 )
									ret := -0.851064 // sell
								if( upper_5 > 25.8128 )
									ret := 0.000000
							if( lower_3 > 24.5487 )
								if( lower_5 <= 24.4035 )
									ret := 0.727273 // buy
								if( lower_5 > 24.4035 )
									ret := -0.298507
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Fibonacci_Bollinger 
//@version=5
//indicator shorttitle="FBB", title="Fibonacci Bollinger Bands", overlay=true)

// Inputs
length_FiboBB = input.int(200, minval=1)
src = input(hlc3, title="Source")
mult = input.float(3.0, minval=0.001, maxval=50)

// Calculations
basis = ta.vwma(src, length_FiboBB)
dev = mult * ta.stdev(src, length_FiboBB)

// Upper Bands
upper_1 = basis + (0.236 * dev)
upper_2 = basis + (0.382 * dev)
upper_3 = basis + (0.5 * dev)
upper_4 = basis + (0.618 * dev)
upper_5 = basis + (0.764 * dev)
upper_6 = basis + (1 * dev)

// Lower Bands
lower_1 = basis - (0.236 * dev)
lower_2 = basis - (0.382 * dev)
lower_3 = basis - (0.5 * dev)
lower_4 = basis - (0.618 * dev)
lower_5 = basis - (0.764 * dev)
lower_6 = basis - (1 * dev)

basis_minus = basis -lower_6
basis_max = basis -upper_6

// Plotting
plot(basis, color=color.fuchsia, linewidth=2)
plot(upper_1, color=color.white, linewidth=1, title="0.236")
plot(upper_2, color=color.white, linewidth=1, title="0.382")
plot(upper_3, color=color.white, linewidth=1, title="0.5")
plot(upper_4, color=color.white, linewidth=1, title="0.618")
plot(upper_5, color=color.white, linewidth=1, title="0.764")
plot(upper_6, color=color.red, linewidth=2, title="1")
plot(lower_1, color=color.white, linewidth=1, title="0.236")
plot(lower_2, color=color.white, linewidth=1, title="0.382")
plot(lower_3, color=color.white, linewidth=1, title="0.5")
plot(lower_4, color=color.white, linewidth=1, title="0.618")
plot(lower_5, color=color.white, linewidth=1, title="0.764")
plot(lower_6, color=color.green, linewidth=2, title="1")

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
float op_operation = decision_tree_0_U_1Min_0e840f96(lower_6, lower_3, basis_max, lower_1, upper_2, upper_6, upper_4, lower_2, basis_minus, upper_3, lower_5, upper_1, lower_4, basis, upper_5)

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



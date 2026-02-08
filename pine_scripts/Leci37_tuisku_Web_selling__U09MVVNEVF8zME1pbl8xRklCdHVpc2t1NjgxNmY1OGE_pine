//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Fibonacci_Bollinger
// ID_model: SOLUSDT_30Min_1FIB_6816f58a Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SOLUSDT_30Min_1FIB_6816f58a", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SOLUSDT_30Min_6816f58a(basis, upper_2, upper_3, lower_2, lower_6, lower_1, basis_minus, lower_3, upper_6, lower_5, lower_4, upper_5, upper_4, basis_max, upper_1)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( basis <= 1.41614 )
		if( basis_minus <= 0.187559 )
			if( lower_3 <= 1.30862 )
				if( lower_1 <= 1.33965 )
					if( lower_4 <= 1.23975 )
						if( lower_5 <= 1.16793 )
							ret := 1.000000 // buy
						if( lower_5 > 1.16793 )
							ret := 0.200000
					if( lower_4 > 1.23975 )
						if( lower_3 <= 1.2904 )
							if( basis <= 1.35302 )
								ret := 0.950000 // buy
							if( basis > 1.35302 )
								ret := 1.000000 // buy
						if( lower_3 > 1.2904 )
							if( lower_5 <= 1.26218 )
								ret := 0.555556
							if( lower_5 > 1.26218 )
								ret := 1.000000 // buy
				if( lower_1 > 1.33965 )
					ret := -0.636364
			if( lower_3 > 1.30862 )
				if( lower_5 <= 1.26619 )
					ret := 0.833333 // buy
				if( lower_5 > 1.26619 )
					ret := 1.000000 // buy
		if( basis_minus > 0.187559 )
			if( lower_1 <= 1.29761 )
				if( lower_4 <= 1.19354 )
					if( lower_4 <= 1.18916 )
						if( lower_4 <= 1.1684 )
							ret := -0.400000
						if( lower_4 > 1.1684 )
							if( upper_4 <= 1.56381 )
								if( basis_max <= -0.281535 )
									ret := -0.380952
								if( basis_max > -0.281535 )
									ret := 0.166667
							if( upper_4 > 1.56381 )
								ret := 0.642857
					if( lower_4 > 1.18916 )
						ret := 0.750000 // buy
				if( lower_4 > 1.19354 )
					if( upper_2 <= 1.38133 )
						ret := -0.571429
					if( upper_2 > 1.38133 )
						if( lower_6 <= 1.12215 )
							ret := 0.235294
						if( lower_6 > 1.12215 )
							ret := -0.272727
			if( lower_1 > 1.29761 )
				if( lower_5 <= 1.25059 )
					if( basis <= 1.40752 )
						if( lower_5 <= 1.10819 )
							if( upper_4 <= 1.649 )
								if( lower_4 <= 1.16036 )
									ret := 0.666667
								if( lower_4 > 1.16036 )
									ret := 1.000000 // buy
							if( upper_4 > 1.649 )
								ret := 0.421053
						if( lower_5 > 1.10819 )
							ret := 0.307692
					if( basis > 1.40752 )
						if( basis <= 1.41369 )
							ret := 1.000000 // buy
						if( basis > 1.41369 )
							if( upper_2 <= 1.49806 )
								ret := 1.000000 // buy
							if( upper_2 > 1.49806 )
								ret := 0.687500
				if( lower_5 > 1.25059 )
					ret := -0.272727
	if( basis > 1.41614 )
		if( lower_1 <= 143.109 )
			if( basis <= 150.202 )
				if( basis <= 148.133 )
					if( basis_minus <= 0.312136 )
						if( basis <= 2.05888 )
							if( basis_minus <= 0.198189 )
								if( basis_minus <= 0.136237 )
									ret := -0.348066
								if( basis_minus > 0.136237 )
									ret := 0.264746
							if( basis_minus > 0.198189 )
								if( upper_2 <= 2.10112 )
									ret := -0.175686
								if( upper_2 > 2.10112 )
									ret := 0.422680
						if( basis > 2.05888 )
							if( lower_6 <= 3.53466 )
								if( basis <= 2.46154 )
									ret := -0.195701
								if( basis > 2.46154 )
									ret := -0.472500
							if( lower_6 > 3.53466 )
								if( lower_2 <= 3.7192 )
									ret := 0.808511 // buy
								if( lower_2 > 3.7192 )
									ret := 0.000000
					if( basis_minus > 0.312136 )
						if( lower_4 <= 12.9824 )
							if( lower_5 <= 12.794 )
								if( lower_5 <= 1.07684 )
									ret := -1.000000 // sell
								if( lower_5 > 1.07684 )
									ret := 0.053406
							if( lower_5 > 12.794 )
								if( upper_5 <= 14.342 )
									ret := 0.750000 // buy
								if( upper_5 > 14.342 )
									ret := -0.647059
						if( lower_4 > 12.9824 )
							if( lower_1 <= 14.7223 )
								if( upper_5 <= 16.4617 )
									ret := -0.021615
								if( upper_5 > 16.4617 )
									ret := -0.514583
							if( lower_1 > 14.7223 )
								if( lower_3 <= 14.7015 )
									ret := 0.387755
								if( lower_3 > 14.7015 )
									ret := 0.008584
				if( basis > 148.133 )
					if( lower_2 <= 137.383 )
						if( upper_5 <= 178.188 )
							if( upper_2 <= 159.442 )
								ret := -0.625000
							if( upper_2 > 159.442 )
								if( lower_1 <= 140.176 )
									ret := -0.700000 // sell
								if( lower_1 > 140.176 )
									ret := -0.985507 // sell
						if( upper_5 > 178.188 )
							if( lower_4 <= 126.149 )
								if( upper_6 <= 191.975 )
									ret := -0.888889 // sell
								if( upper_6 > 191.975 )
									ret := -0.166667
							if( lower_4 > 126.149 )
								ret := 0.066667
					if( lower_2 > 137.383 )
						ret := 0.647059
			if( basis > 150.202 )
				if( basis_max <= -40.0176 )
					ret := -0.571429
				if( basis_max > -40.0176 )
					if( upper_6 <= 188.758 )
						if( lower_3 <= 132.183 )
							ret := 1.000000 // buy
						if( lower_3 > 132.183 )
							if( upper_1 <= 160.035 )
								ret := 0.800000 // buy
							if( upper_1 > 160.035 )
								ret := 1.000000 // buy
					if( upper_6 > 188.758 )
						if( upper_5 <= 181.174 )
							ret := 0.363636
						if( upper_5 > 181.174 )
							if( lower_4 <= 126.646 )
								ret := 1.000000 // buy
							if( lower_4 > 126.646 )
								ret := 0.875000 // buy
		if( lower_1 > 143.109 )
			if( lower_4 <= 149.167 )
				if( lower_4 <= 143.22 )
					if( lower_4 <= 141.476 )
						if( upper_1 <= 146.366 )
							if( upper_4 <= 148.509 )
								if( lower_5 <= 140.232 )
									ret := 0.909091 // buy
								if( lower_5 > 140.232 )
									ret := 0.304348
							if( upper_4 > 148.509 )
								ret := 0.944444 // buy
						if( upper_1 > 146.366 )
							if( upper_4 <= 149.612 )
								if( lower_4 <= 141.062 )
									ret := -0.800000 // sell
								if( lower_4 > 141.062 )
									ret := -0.527273
							if( upper_4 > 149.612 )
								if( lower_1 <= 163.203 )
									ret := -0.086857
								if( lower_1 > 163.203 )
									ret := -0.962963 // sell
					if( lower_4 > 141.476 )
						if( lower_5 <= 140.194 )
							if( upper_4 <= 200.335 )
								if( basis_minus <= 10.2577 )
									ret := 0.883721 // buy
								if( basis_minus > 10.2577 )
									ret := 0.331210
							if( upper_4 > 200.335 )
								ret := -1.000000 // sell
						if( lower_5 > 140.194 )
							if( lower_5 <= 141.219 )
								if( basis_minus <= 7.017 )
									ret := 0.391304
								if( basis_minus > 7.017 )
									ret := 0.046358
							if( lower_5 > 141.219 )
								if( upper_4 <= 149.297 )
									ret := 0.583333
								if( upper_4 > 149.297 )
									ret := -0.329412
				if( lower_4 > 143.22 )
					if( upper_3 <= 182.849 )
						if( lower_1 <= 153.816 )
							if( lower_4 <= 144.588 )
								if( upper_6 <= 166.068 )
									ret := -0.281609
								if( upper_6 > 166.068 )
									ret := -0.639456
							if( lower_4 > 144.588 )
								if( upper_1 <= 155.811 )
									ret := 0.868421 // buy
								if( upper_1 > 155.811 )
									ret := -0.170588
						if( lower_1 > 153.816 )
							if( upper_2 <= 172.808 )
								if( lower_4 <= 143.768 )
									ret := -1.000000 // sell
								if( lower_4 > 143.768 )
									ret := -0.663265
							if( upper_2 > 172.808 )
								if( lower_6 <= 133.416 )
									ret := -0.794872 // sell
								if( lower_6 > 133.416 )
									ret := -0.308411
					if( upper_3 > 182.849 )
						if( upper_4 <= 188.44 )
							if( lower_2 <= 155.418 )
								if( basis_minus <= 32.3982 )
									ret := 0.750000 // buy
								if( basis_minus > 32.3982 )
									ret := 1.000000 // buy
							if( lower_2 > 155.418 )
								if( lower_3 <= 151.908 )
									ret := -0.766667 // sell
								if( lower_3 > 151.908 )
									ret := 0.550000
						if( upper_4 > 188.44 )
							if( lower_1 <= 159.336 )
								ret := 0.631579
							if( lower_1 > 159.336 )
								if( basis <= 179.384 )
									ret := -0.568000
								if( basis > 179.384 )
									ret := 0.310345
			if( lower_4 > 149.167 )
				if( basis_minus <= 34.6228 )
					if( lower_6 <= 142.823 )
						if( lower_3 <= 153.048 )
							if( lower_3 <= 151.742 )
								if( basis_max <= -20.3179 )
									ret := 0.863636 // buy
								if( basis_max > -20.3179 )
									ret := 1.000000 // buy
							if( lower_3 > 151.742 )
								if( lower_3 <= 151.768 )
									ret := -0.758621 // sell
								if( lower_3 > 151.768 )
									ret := 0.712871 // buy
						if( lower_3 > 153.048 )
							if( upper_5 <= 195.26 )
								if( upper_4 <= 188.344 )
									ret := 0.105263
								if( upper_4 > 188.344 )
									ret := -0.745098 // sell
							if( upper_5 > 195.26 )
								if( upper_5 <= 196.272 )
									ret := 0.846154 // buy
								if( upper_5 > 196.272 )
									ret := 0.600000
					if( lower_6 > 142.823 )
						if( lower_3 <= 154.546 )
							if( basis_max <= -17.7641 )
								if( basis_max <= -21.4114 )
									ret := -1.000000 // sell
								if( basis_max > -21.4114 )
									ret := -0.707692 // sell
							if( basis_max > -17.7641 )
								if( lower_6 <= 144.423 )
									ret := 0.581395
								if( lower_6 > 144.423 )
									ret := -0.275000
						if( lower_3 > 154.546 )
							if( lower_5 <= 151.941 )
								if( upper_6 <= 177.06 )
									ret := 0.730159 // buy
								if( upper_6 > 177.06 )
									ret := 0.296820
							if( lower_5 > 151.941 )
								if( basis_minus <= 33.3333 )
									ret := -0.027906
								if( basis_minus > 33.3333 )
									ret := -0.478448
				if( basis_minus > 34.6228 )
					if( upper_4 <= 207.904 )
						if( basis <= 174.89 )
							if( lower_2 <= 159.178 )
								ret := 1.000000 // buy
							if( lower_2 > 159.178 )
								ret := 0.800000 // buy
						if( basis > 174.89 )
							if( lower_4 <= 153.011 )
								if( basis_minus <= 39.0054 )
									ret := -0.333333
								if( basis_minus > 39.0054 )
									ret := 0.100000
							if( lower_4 > 153.011 )
								if( upper_2 <= 197.305 )
									ret := 0.461538
								if( upper_2 > 197.305 )
									ret := 0.894737 // buy
					if( upper_4 > 207.904 )
						if( lower_6 <= 170.228 )
							if( lower_4 <= 173.333 )
								if( basis <= 198.548 )
									ret := -0.049419
								if( basis > 198.548 )
									ret := 0.763636 // buy
							if( lower_4 > 173.333 )
								if( lower_3 <= 182.895 )
									ret := -0.771930 // sell
								if( lower_3 > 182.895 )
									ret := -0.039604
						if( lower_6 > 170.228 )
							if( lower_2 <= 203.495 )
								if( lower_1 <= 206.148 )
									ret := 0.371134
								if( lower_1 > 206.148 )
									ret := 0.682171
							if( lower_2 > 203.495 )
								if( upper_2 <= 247.021 )
									ret := -0.425926
								if( upper_2 > 247.021 )
									ret := 0.822222 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_SOLUSDT_30Min_6816f58a(basis, upper_2, upper_3, lower_2, lower_6, lower_1, basis_minus, lower_3, upper_6, lower_5, lower_4, upper_5, upper_4, basis_max, upper_1)

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



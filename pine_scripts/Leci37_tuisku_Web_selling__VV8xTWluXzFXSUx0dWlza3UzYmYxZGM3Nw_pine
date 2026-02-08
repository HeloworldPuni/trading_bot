//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Williams_Vix_Fix
// ID_model: U_1Min_1WIL_3bf1dc77 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_U_1Min_1WIL_3bf1dc77", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_U_1Min_3bf1dc77(rangeLow, wvf, Color_con1, midLine, sDev, colInt, upperBand, rangeHigh, lowerBand, Color_con2)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7, max_features=0.82,min_samples_leaf=7, min_samples_split=10,random_state=843828734)
	if( wvf <= 0.015864 )
		if( sDev <= 0.074276 )
			if( sDev <= 0.068521 )
				ret := -0.083333
			if( sDev > 0.068521 )
				if( wvf <= 0.000184 )
					ret := 0.454545
				if( wvf > 0.000184 )
					if( Color_con2 <= -0.215638 )
						ret := 0.857143 // buy
					if( Color_con2 > -0.215638 )
						ret := 1.000000 // buy
		if( sDev > 0.074276 )
			if( lowerBand <= 0.108192 )
				if( Color_con2 <= -0.250782 )
					if( Color_con1 <= -0.414704 )
						if( lowerBand <= 0.056483 )
							if( upperBand <= 0.481362 )
								ret := -0.461538
							if( upperBand > 0.481362 )
								ret := -0.212963
						if( lowerBand > 0.056483 )
							if( wvf <= 0.000826 )
								ret := -0.037037
							if( wvf > 0.000826 )
								ret := 0.733333 // buy
					if( Color_con1 > -0.414704 )
						if( lowerBand <= -0.137117 )
							if( Color_con2 <= -0.411616 )
								ret := 0.142857
							if( Color_con2 > -0.411616 )
								ret := 0.705882 // buy
						if( lowerBand > -0.137117 )
							if( midLine <= 0.10716 )
								ret := -0.311203
							if( midLine > 0.10716 )
								ret := 0.021661
				if( Color_con2 > -0.250782 )
					if( Color_con1 <= -0.20703 )
						if( lowerBand <= -0.032272 )
							if( sDev <= 0.301826 )
								ret := -0.511811
							if( sDev > 0.301826 )
								ret := -0.843750 // sell
						if( lowerBand > -0.032272 )
							if( lowerBand <= -0.002046 )
								ret := 0.157895
							if( lowerBand > -0.002046 )
								ret := -0.562500
					if( Color_con1 > -0.20703 )
						if( Color_con2 <= -0.161317 )
							if( Color_con1 <= -0.187563 )
								ret := -0.050000
							if( Color_con1 > -0.187563 )
								ret := -0.450000
						if( Color_con2 > -0.161317 )
							if( sDev <= 0.115945 )
								ret := -0.161290
							if( sDev > 0.115945 )
								ret := 0.909091 // buy
			if( lowerBand > 0.108192 )
				if( lowerBand <= 0.189818 )
					if( lowerBand <= 0.11497 )
						ret := -0.583333
					if( lowerBand > 0.11497 )
						if( Color_con2 <= -0.832975 )
							if( Color_con2 <= -1.19314 )
								ret := -0.857143 // sell
							if( Color_con2 > -1.19314 )
								ret := -0.500000
						if( Color_con2 > -0.832975 )
							ret := -1.000000 // sell
				if( lowerBand > 0.189818 )
					ret := -0.416667
	if( wvf > 0.015864 )
		if( Color_con2 <= -0.196925 )
			if( wvf <= 0.243964 )
				if( sDev <= 0.067517 )
					if( Color_con2 <= -0.353987 )
						if( lowerBand <= -0.006459 )
							ret := -0.750000 // sell
						if( lowerBand > -0.006459 )
							if( upperBand <= 0.141816 )
								ret := 0.000000
							if( upperBand > 0.141816 )
								ret := 0.375000
					if( Color_con2 > -0.353987 )
						if( upperBand <= 0.136672 )
							if( upperBand <= 0.107876 )
								ret := 0.791667 // buy
							if( upperBand > 0.107876 )
								ret := -0.045455
						if( upperBand > 0.136672 )
							if( lowerBand <= 0.00882 )
								ret := 0.571429
							if( lowerBand > 0.00882 )
								ret := 1.000000 // buy
				if( sDev > 0.067517 )
					if( Color_con2 <= -3.23975 )
						if( Color_con2 <= -3.90089 )
							if( lowerBand <= -0.070718 )
								ret := -0.473684
							if( lowerBand > -0.070718 )
								ret := 0.100000
						if( Color_con2 > -3.90089 )
							if( Color_con2 <= -3.59151 )
								ret := -0.961538 // sell
							if( Color_con2 > -3.59151 )
								ret := -0.625000
					if( Color_con2 > -3.23975 )
						if( Color_con1 <= -2.97855 )
							if( upperBand <= 4.38541 )
								ret := 0.663265
							if( upperBand > 4.38541 )
								ret := -0.125000
						if( Color_con1 > -2.97855 )
							if( upperBand <= 2.45138 )
								ret := -0.014876
							if( upperBand > 2.45138 )
								ret := -0.423077
			if( wvf > 0.243964 )
				if( Color_con2 <= -4.84639 )
					if( lowerBand <= -0.298359 )
						if( wvf <= 2.48753 )
							if( Color_con1 <= -8.01384 )
								ret := -0.705882 // sell
							if( Color_con1 > -8.01384 )
								ret := -0.987179 // sell
						if( wvf > 2.48753 )
							if( upperBand <= 10.5355 )
								ret := -0.285714
							if( upperBand > 10.5355 )
								ret := -1.000000 // sell
					if( lowerBand > -0.298359 )
						if( wvf <= 1.79658 )
							if( Color_con1 <= -10.5153 )
								ret := 1.000000 // buy
							if( Color_con1 > -10.5153 )
								ret := -0.333333
						if( wvf > 1.79658 )
							if( Color_con2 <= -5.39874 )
								ret := 1.000000 // buy
							if( Color_con2 > -5.39874 )
								ret := 0.875000 // buy
				if( Color_con2 > -4.84639 )
					if( Color_con2 <= -4.10909 )
						if( midLine <= 5.95731 )
							if( midLine <= 2.82689 )
								ret := 0.355556
							if( midLine > 2.82689 )
								ret := 0.949153 // buy
						if( midLine > 5.95731 )
							ret := -0.200000
					if( Color_con2 > -4.10909 )
						if( Color_con2 <= -3.35154 )
							if( lowerBand <= 1.3754 )
								ret := -0.556604
							if( lowerBand > 1.3754 )
								ret := 0.466667
						if( Color_con2 > -3.35154 )
							if( lowerBand <= 1.24907 )
								ret := 0.057083
							if( lowerBand > 1.24907 )
								ret := -0.249035
		if( Color_con2 > -0.196925 )
			if( sDev <= 0.859151 )
				if( upperBand <= 0.177627 )
					if( Color_con2 <= -0.095355 )
						if( Color_con2 <= -0.125467 )
							if( Color_con1 <= -0.032244 )
								ret := 0.126984
							if( Color_con1 > -0.032244 )
								ret := 0.627907
						if( Color_con2 > -0.125467 )
							if( lowerBand <= -0.033852 )
								ret := 0.000000
							if( lowerBand > -0.033852 )
								ret := 0.621951
					if( Color_con2 > -0.095355 )
						if( Color_con1 <= -0.065003 )
							if( lowerBand <= 0.011508 )
								ret := 0.031746
							if( lowerBand > 0.011508 )
								ret := -0.642857
						if( Color_con1 > -0.065003 )
							if( upperBand <= 0.171286 )
								ret := 0.133333
							if( upperBand > 0.171286 )
								ret := 0.615385
				if( upperBand > 0.177627 )
					if( lowerBand <= -0.203635 )
						if( wvf <= 1.45906 )
							if( lowerBand <= -0.366637 )
								ret := -0.053097
							if( lowerBand > -0.366637 )
								ret := 0.296960
						if( wvf > 1.45906 )
							if( lowerBand <= -0.370269 )
								ret := 0.136364
							if( lowerBand > -0.370269 )
								ret := -0.554217
					if( lowerBand > -0.203635 )
						if( lowerBand <= 0.765788 )
							if( midLine <= 1.34291 )
								ret := 0.069123
							if( midLine > 1.34291 )
								ret := 0.788732 // buy
						if( lowerBand > 0.765788 )
							if( Color_con1 <= -0.797383 )
								ret := 0.866667 // buy
							if( Color_con1 > -0.797383 )
								ret := -0.142857
			if( sDev > 0.859151 )
				if( sDev <= 1.10126 )
					if( Color_con2 <= 1.06079 )
						if( lowerBand <= -0.370508 )
							if( Color_con2 <= -0.135142 )
								ret := -0.333333
							if( Color_con2 > -0.135142 )
								ret := 0.725490 // buy
						if( lowerBand > -0.370508 )
							if( Color_con2 <= 1.02089 )
								ret := 0.329977
							if( Color_con2 > 1.02089 )
								ret := -0.777778 // sell
					if( Color_con2 > 1.06079 )
						if( wvf <= 1.8248 )
							if( wvf <= 1.57639 )
								ret := -1.000000 // sell
							if( wvf > 1.57639 )
								ret := -0.323529
						if( wvf > 1.8248 )
							if( wvf <= 2.19039 )
								ret := 0.625000
							if( wvf > 2.19039 )
								ret := 0.083333
				if( sDev > 1.10126 )
					if( upperBand <= 2.07413 )
						if( upperBand <= 1.56713 )
							if( Color_con1 <= -1.1478 )
								ret := 0.142857
							if( Color_con1 > -1.1478 )
								ret := 0.857143 // buy
						if( upperBand > 1.56713 )
							if( wvf <= 1.82989 )
								ret := -0.428571
							if( wvf > 1.82989 )
								ret := 0.050505
					if( upperBand > 2.07413 )
						if( Color_con1 <= -0.730337 )
							if( lowerBand <= -0.639073 )
								ret := 0.014354
							if( lowerBand > -0.639073 )
								ret := 0.410326
						if( Color_con1 > -0.730337 )
							if( sDev <= 1.50521 )
								ret := -0.112245
							if( sDev > 1.50521 )
								ret := 0.290572
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Williams_Vix_Fix 
//@version=5
//indicator "CM_Williams_Vix_Fix", overlay=false)

// Inputs
pd = input.int(22, title="LookBack Period Standard Deviation High")
bbl = input.int(20, title="Bollinger Band Length")
mult = input.float(2.0, minval=1, maxval=5, title="Bollinger Band Standard Deviation Up")
lb = input.int(50, title="Look Back Period Percentile High")
ph = input.float(0.85, title="Highest Percentile - 0.90=90%, 0.95=95%, 0.99=99%")
pl = input.float(1.01, title="Lowest Percentile - 1.10=90%, 1.05=95%, 1.01=99%")
hp = input.bool(false, title="Show High Range - Based on Percentile and LookBack Period?")
sd = input.bool(false, title="Show Standard Deviation Line?")

// Calculations
wvf = ((ta.highest(close, pd) - low) / ta.highest(close, pd)) * 100

sDev = mult * ta.stdev(wvf, bbl)
midLine = ta.sma(wvf, bbl)
lowerBand = midLine - sDev
upperBand = midLine + sDev

rangeHigh = ta.highest(wvf, lb) * ph
rangeLow = ta.lowest(wvf, lb) * pl


Color_con1 = wvf - upperBand
Color_con2 = wvf - rangeHigh
// Color condition
col = wvf >= upperBand or wvf >= rangeHigh ? color.lime : color.gray
colInt = wvf >= upperBand or wvf >= rangeHigh ? 1 : 0 //Bool to int

// Plots
plot(hp and na(rangeHigh) ? na : rangeHigh, title="Range High Percentile", color=color.orange, linewidth=4)
plot(hp and na(rangeLow) ? na : rangeLow, title="Range Low Percentile", color=color.orange, linewidth=4)
plot(wvf, title="Williams Vix Fix", color=col, style=plot.style_histogram, linewidth=4)
plot(sd and na(upperBand) ? na : upperBand, title="Upper Band", color=color.aqua, linewidth=3)

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
float op_operation = decision_tree_0_U_1Min_3bf1dc77(rangeLow, wvf, Color_con1, midLine, sDev, colInt, upperBand, rangeHigh, lowerBand, Color_con2)

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



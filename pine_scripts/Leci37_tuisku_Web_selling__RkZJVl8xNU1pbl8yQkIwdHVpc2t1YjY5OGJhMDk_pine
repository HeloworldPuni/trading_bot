//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bollinger_Bands, L_Bull_Bear_Power
// ID_model: FFIV_15Min_2BB0_b698ba09 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_FFIV_15Min_2BB0_b698ba09", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_FFIV_15Min_b698ba09(basis, Upper_Band, Lower_Band, bearPower, bbm, bbp, bullPower, BBPower_Color)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( Lower_Band <= 142.471 )
		if( Lower_Band <= 86.4604 )
			ret := 1.000000 // buy
		if( Lower_Band > 86.4604 )
			if( Upper_Band <= 166.317 )
				if( Lower_Band <= 140.114 )
					if( bullPower <= 1.86248 )
						if( bbp <= 0.329167 )
							if( basis <= 106.794 )
								if( basis <= 100.361 )
									ret := 0.144330
								if( basis > 100.361 )
									ret := 0.666667
							if( basis > 106.794 )
								if( Lower_Band <= 114.044 )
									ret := -0.301887
								if( Lower_Band > 114.044 )
									ret := 0.054753
						if( bbp > 0.329167 )
							if( basis <= 127.351 )
								if( bullPower <= 1.31085 )
									ret := 0.282712
								if( bullPower > 1.31085 )
									ret := -0.057377
							if( basis > 127.351 )
								if( bbm <= 0.542979 )
									ret := 0.054994
								if( bbm > 0.542979 )
									ret := 0.225980
					if( bullPower > 1.86248 )
						if( bbp <= 5.99737 )
							if( Lower_Band <= 116.699 )
								if( bbm <= 0.91329 )
									ret := -0.948718 // sell
								if( bbm > 0.91329 )
									ret := -0.276923
							if( Lower_Band > 116.699 )
								if( bbm <= 1.805 )
									ret := -0.148734
								if( bbm > 1.805 )
									ret := 0.337500
						if( bbp > 5.99737 )
							if( Lower_Band <= 132.239 )
								if( Upper_Band <= 112.751 )
									ret := -0.800000 // sell
								if( Upper_Band > 112.751 )
									ret := 0.734043 // buy
							if( Lower_Band > 132.239 )
								if( Lower_Band <= 138.204 )
									ret := -0.350000
								if( Lower_Band > 138.204 )
									ret := 0.625000
				if( Lower_Band > 140.114 )
					if( bbp <= -2.84058 )
						if( bbp <= -4.91436 )
							if( basis <= 145.303 )
								if( bullPower <= -1.78393 )
									ret := -0.500000
								if( bullPower > -1.78393 )
									ret := -1.000000 // sell
							if( basis > 145.303 )
								if( basis <= 145.487 )
									ret := 1.000000 // buy
								if( basis > 145.487 )
									ret := 0.111111
						if( bbp > -4.91436 )
							if( basis <= 143.614 )
								if( Upper_Band <= 146.094 )
									ret := 1.000000 // buy
								if( Upper_Band > 146.094 )
									ret := 0.500000
							if( basis > 143.614 )
								if( Upper_Band <= 148.794 )
									ret := -0.368421
								if( Upper_Band > 148.794 )
									ret := 0.653846
					if( bbp > -2.84058 )
						if( basis <= 142.224 )
							if( basis <= 141.757 )
								if( Lower_Band <= 140.67 )
									ret := 0.301318
								if( Lower_Band > 140.67 )
									ret := -0.246914
							if( basis > 141.757 )
								if( Upper_Band <= 142.913 )
									ret := 0.281081
								if( Upper_Band > 142.913 )
									ret := 0.558065
						if( basis > 142.224 )
							if( Lower_Band <= 140.781 )
								if( Lower_Band <= 140.329 )
									ret := 0.255814
								if( Lower_Band > 140.329 )
									ret := -0.226891
							if( Lower_Band > 140.781 )
								if( bbp <= -2.30623 )
									ret := -0.390244
								if( bbp > -2.30623 )
									ret := 0.135268
			if( Upper_Band > 166.317 )
				if( bbm <= 0.893523 )
					if( basis <= 153.13 )
						ret := -1.000000 // sell
					if( basis > 153.13 )
						ret := 0.714286 // buy
				if( bbm > 0.893523 )
					ret := -1.000000 // sell
	if( Lower_Band > 142.471 )
		if( basis <= 148.426 )
			if( Upper_Band <= 149 )
				if( bearPower <= 0.713002 )
					if( bbm <= 1.8073 )
						if( bbp <= 1.60248 )
							if( basis <= 148.188 )
								if( bearPower <= 0.589005 )
									ret := -0.009427
								if( bearPower > 0.589005 )
									ret := -0.557377
							if( basis > 148.188 )
								if( bearPower <= -0.37393 )
									ret := 1.000000 // buy
								if( bearPower > -0.37393 )
									ret := 0.461538
						if( bbp > 1.60248 )
							if( bearPower <= 0.60743 )
								if( Lower_Band <= 146.044 )
									ret := 0.662791
								if( Lower_Band > 146.044 )
									ret := -0.200000
							if( bearPower > 0.60743 )
								if( basis <= 146.318 )
									ret := 0.428571
								if( basis > 146.318 )
									ret := -0.125000
					if( bbm > 1.8073 )
						if( bullPower <= 0.778345 )
							if( basis <= 145.178 )
								ret := -0.428571
							if( basis > 145.178 )
								ret := -1.000000 // sell
						if( bullPower > 0.778345 )
							if( bullPower <= 0.974075 )
								ret := 0.750000 // buy
							if( bullPower > 0.974075 )
								if( basis <= 146.741 )
									ret := -0.631579
								if( basis > 146.741 )
									ret := 0.000000
				if( bearPower > 0.713002 )
					if( Upper_Band <= 147.658 )
						if( Lower_Band <= 142.895 )
							if( basis <= 144.448 )
								if( bbm <= 0.57 )
									ret := 0.000000
								if( bbm > 0.57 )
									ret := 0.833333 // buy
							if( basis > 144.448 )
								ret := -0.250000
						if( Lower_Band > 142.895 )
							if( basis <= 145.531 )
								if( bbm <= 0.345 )
									ret := -0.750000 // sell
								if( bbm > 0.345 )
									ret := -1.000000 // sell
							if( basis > 145.531 )
								if( basis <= 146.26 )
									ret := -0.272727
								if( basis > 146.26 )
									ret := -0.933333 // sell
					if( Upper_Band > 147.658 )
						if( bullPower <= 2.09572 )
							if( bbp <= 1.94406 )
								if( bullPower <= 1.0759 )
									ret := -0.250000
								if( bullPower > 1.0759 )
									ret := -1.000000 // sell
							if( bbp > 1.94406 )
								if( bbm <= 0.677054 )
									ret := 0.363636
								if( bbm > 0.677054 )
									ret := -0.375000
						if( bullPower > 2.09572 )
							if( bbm <= 0.539526 )
								ret := -1.000000 // sell
							if( bbm > 0.539526 )
								ret := -0.500000
			if( Upper_Band > 149 )
				if( basis <= 146.549 )
					if( bearPower <= -1.78809 )
						if( bullPower <= -1.03108 )
							ret := 0.714286 // buy
						if( bullPower > -1.03108 )
							ret := -0.250000
					if( bearPower > -1.78809 )
						if( basis <= 146.521 )
							if( bbm <= 0.369498 )
								ret := -0.500000
							if( bbm > 0.369498 )
								if( Upper_Band <= 149.14 )
									ret := -0.818182 // sell
								if( Upper_Band > 149.14 )
									ret := -0.974359 // sell
						if( basis > 146.521 )
							if( bbm <= 0.4475 )
								ret := 0.250000
							if( bbm > 0.4475 )
								ret := -0.857143 // sell
				if( basis > 146.549 )
					if( bullPower <= 0.306515 )
						if( Lower_Band <= 143.671 )
							if( bearPower <= -2.27133 )
								ret := -0.250000
							if( bearPower > -2.27133 )
								if( basis <= 147.509 )
									ret := -0.958333 // sell
								if( basis > 147.509 )
									ret := -0.250000
						if( Lower_Band > 143.671 )
							if( bbp <= -2.15847 )
								if( bbm <= 0.095658 )
									ret := -1.000000 // sell
								if( bbm > 0.095658 )
									ret := 0.342857
							if( bbp > -2.15847 )
								if( Upper_Band <= 150.941 )
									ret := -0.126943
								if( Upper_Band > 150.941 )
									ret := 0.888889 // buy
					if( bullPower > 0.306515 )
						if( Upper_Band <= 150.385 )
							if( bearPower <= 1.00674 )
								if( Lower_Band <= 144.314 )
									ret := 0.160000
								if( Lower_Band > 144.314 )
									ret := -0.406593
							if( bearPower > 1.00674 )
								if( bullPower <= 1.50702 )
									ret := -0.833333 // sell
								if( bullPower > 1.50702 )
									ret := -1.000000 // sell
						if( Upper_Band > 150.385 )
							if( bearPower <= 0.443133 )
								if( basis <= 148.088 )
									ret := 0.250000
								if( basis > 148.088 )
									ret := -0.923077 // sell
							if( bearPower > 0.443133 )
								if( bullPower <= 1.41075 )
									ret := 1.000000 // buy
								if( bullPower > 1.41075 )
									ret := 0.571429
		if( basis > 148.426 )
			if( Lower_Band <= 149.754 )
				if( bbp <= 1.05523 )
					if( bbp <= -5.52875 )
						if( Lower_Band <= 149.195 )
							if( Upper_Band <= 154.977 )
								ret := -0.200000
							if( Upper_Band > 154.977 )
								if( Upper_Band <= 165.503 )
									ret := -1.000000 // sell
								if( Upper_Band > 165.503 )
									ret := -0.428571
						if( Lower_Band > 149.195 )
							ret := 0.142857
					if( bbp > -5.52875 )
						if( basis <= 155.189 )
							if( Upper_Band <= 151.498 )
								if( Lower_Band <= 148.81 )
									ret := 0.118690
								if( Lower_Band > 148.81 )
									ret := -0.504950
							if( Upper_Band > 151.498 )
								if( Lower_Band <= 148.906 )
									ret := 0.080000
								if( Lower_Band > 148.906 )
									ret := 0.368590
						if( basis > 155.189 )
							ret := 1.000000 // buy
				if( bbp > 1.05523 )
					if( bbm <= 1.80746 )
						if( Lower_Band <= 148.96 )
							if( Lower_Band <= 148.011 )
								if( bullPower <= 1.51896 )
									ret := 0.261364
								if( bullPower > 1.51896 )
									ret := 0.677778
							if( Lower_Band > 148.011 )
								if( bullPower <= 1.25086 )
									ret := -0.466667
								if( bullPower > 1.25086 )
									ret := 0.219512
						if( Lower_Band > 148.96 )
							if( bullPower <= 1.70396 )
								if( basis <= 151.698 )
									ret := 0.885714 // buy
								if( basis > 151.698 )
									ret := 0.393939
							if( bullPower > 1.70396 )
								if( bearPower <= 1.37181 )
									ret := 0.250000
								if( bearPower > 1.37181 )
									ret := -0.800000 // sell
					if( bbm > 1.80746 )
						if( bbm <= 5.96789 )
							if( bbp <= 5.37301 )
								ret := -0.500000
							if( bbp > 5.37301 )
								ret := -1.000000 // sell
						if( bbm > 5.96789 )
							ret := 0.000000
			if( Lower_Band > 149.754 )
				if( bbm <= 0.11055 )
					if( bbp <= -0.59652 )
						if( Lower_Band <= 213.978 )
							if( Lower_Band <= 202.886 )
								if( Upper_Band <= 211.046 )
									ret := 0.315024
								if( Upper_Band > 211.046 )
									ret := -0.684211
							if( Lower_Band > 202.886 )
								if( Upper_Band <= 206.678 )
									ret := -1.000000 // sell
								if( Upper_Band > 206.678 )
									ret := -0.100000
						if( Lower_Band > 213.978 )
							if( Lower_Band <= 231.375 )
								if( bbp <= -0.891802 )
									ret := 0.790698 // buy
								if( bbp > -0.891802 )
									ret := 0.400000
							if( Lower_Band > 231.375 )
								if( Upper_Band <= 240.21 )
									ret := -0.500000
								if( Upper_Band > 240.21 )
									ret := 0.600000
					if( bbp > -0.59652 )
						if( Lower_Band <= 180.043 )
							if( Lower_Band <= 179.656 )
								if( Lower_Band <= 178.895 )
									ret := 0.175472
								if( Lower_Band > 178.895 )
									ret := -0.571429
							if( Lower_Band > 179.656 )
								if( bearPower <= 0.066057 )
									ret := 0.444444
								if( bearPower > 0.066057 )
									ret := 0.941176 // buy
						if( Lower_Band > 180.043 )
							if( Lower_Band <= 181.65 )
								if( Upper_Band <= 182.309 )
									ret := -1.000000 // sell
								if( Upper_Band > 182.309 )
									ret := -0.583333
							if( Lower_Band > 181.65 )
								if( Upper_Band <= 202.771 )
									ret := -0.130435
								if( Upper_Band > 202.771 )
									ret := 0.112994
				if( bbm > 0.11055 )
					if( basis <= 151.901 )
						if( basis <= 151.464 )
							if( basis <= 151.175 )
								if( bearPower <= -0.09687 )
									ret := -0.671875
								if( bearPower > -0.09687 )
									ret := 0.121212
							if( basis > 151.175 )
								if( bbp <= 1.06169 )
									ret := 0.260417
								if( bbp > 1.06169 )
									ret := -0.611111
						if( basis > 151.464 )
							if( Lower_Band <= 149.947 )
								if( bbp <= 0.602445 )
									ret := 0.583333
								if( bbp > 0.602445 )
									ret := -0.166667
							if( Lower_Band > 149.947 )
								if( Lower_Band <= 150.439 )
									ret := -0.700000 // sell
								if( Lower_Band > 150.439 )
									ret := -0.402174
					if( basis > 151.901 )
						if( bearPower <= -2.66343 )
							if( Lower_Band <= 182.312 )
								if( bbp <= -3.95227 )
									ret := -0.002762
								if( bbp > -3.95227 )
									ret := 0.555556
							if( Lower_Band > 182.312 )
								if( bbp <= -16.7595 )
									ret := -0.636364
								if( bbp > -16.7595 )
									ret := 0.377404
						if( bearPower > -2.66343 )
							if( bbp <= 5.35938 )
								if( bbp <= 1.41149 )
									ret := 0.024693
								if( bbp > 1.41149 )
									ret := -0.037780
							if( bbp > 5.35938 )
								if( Lower_Band <= 189.832 )
									ret := -0.147541
								if( Lower_Band > 189.832 )
									ret := -0.500000
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Bollinger_Bands 
//@version=5
//indicator shorttitle="BB", title="Bollinger Bands", overlay=true, timeframe="", timeframe_gaps=true)
length_BB = input.int(20, minval=1)
maType = input.string("SMA", "Basis MA Type", options = ["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"])
src = input(close, title="Source")
mult = input.float(2.0, minval=0.001, maxval=50, title="StdDev")

ma(source, length_BB, _type) =>
    switch _type
        "SMA" => ta.sma(source, length_BB)
        "EMA" => ta.ema(source, length_BB)
        "SMMA (RMA)" => ta.rma(source, length_BB)
        "WMA" => ta.wma(source, length_BB)
        "VWMA" => ta.vwma(source, length_BB)

basis = ma(src, length_BB, maType)
dev = mult * ta.stdev(src, length_BB)
Upper_Band = basis + dev
Lower_Band = basis - dev
offset = input.int(0, "Offset", minval = -500, maxval = 500, display = display.data_window)
plot(basis, "Basis", color=#2962FF, offset = offset)
p1 = plot(Upper_Band, "Upper", color=#F23645, offset = offset)
p2 = plot(Lower_Band, "Lower", color=#089981, offset = offset)
fill(p1, p2, title = "Background", color=color.rgb(33, 150, 243, 95))

//CODE associated with the technical indicator L_Bull_Bear_Power 
//@version=5
//indicator "Bull Bear Power", shorttitle="BBP")
lengthInput = input.int(13, title="Length")
bullPower = high - ta.ema(close, lengthInput)
bearPower = low - ta.ema(close, lengthInput)
bbp = bullPower + bearPower

bbm = bullPower - bearPower

plot(bbp, color = bbp >= 0 ? #089981 : #f23645, title="BBPower", style = plot.style_columns)
hline(0, "Zero line")

BBPower_Color = bbp >= 0  ? 1: 0

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
float op_operation = decision_tree_0_FFIV_15Min_b698ba09(basis, Upper_Band, Lower_Band, bearPower, bbm, bbp, bullPower, BBPower_Color)

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



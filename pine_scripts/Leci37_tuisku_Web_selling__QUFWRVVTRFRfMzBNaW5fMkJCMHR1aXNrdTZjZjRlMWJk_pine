//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bollinger_Bands, L_Bull_Bear_Power
// ID_model: AAVEUSDT_30Min_2BB0_6cf4e1bd Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AAVEUSDT_30Min_2BB0_6cf4e1bd", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AAVEUSDT_30Min_6cf4e1bd(Upper_Band, basis, Lower_Band, bullPower, bbp, bearPower, bbm, BBPower_Color)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7, max_features=0.82,min_samples_leaf=7, min_samples_split=10,random_state=843828734)
	if( Upper_Band <= 409.762 )
		if( bearPower <= -4.94996 )
			if( Upper_Band <= 88.0179 )
				if( Upper_Band <= 71.2725 )
					if( Lower_Band <= 56.5777 )
						ret := 1.000000 // buy
					if( Lower_Band > 56.5777 )
						if( bbp <= -6.46667 )
							ret := -0.500000
						if( bbp > -6.46667 )
							ret := 0.857143 // buy
				if( Upper_Band > 71.2725 )
					if( Lower_Band <= 76.9261 )
						if( Lower_Band <= 67.8837 )
							ret := 0.857143 // buy
						if( Lower_Band > 67.8837 )
							ret := 1.000000 // buy
					if( Lower_Band > 76.9261 )
						ret := 0.500000
			if( Upper_Band > 88.0179 )
				if( bbm <= 8.6306 )
					if( Upper_Band <= 385.67 )
						if( Upper_Band <= 360.345 )
							if( Lower_Band <= 313.597 )
								ret := 0.160515
							if( Lower_Band > 313.597 )
								ret := -0.268571
						if( Upper_Band > 360.345 )
							if( bearPower <= -8.49588 )
								ret := 0.728682 // buy
							if( bearPower > -8.49588 )
								ret := 0.356322
					if( Upper_Band > 385.67 )
						if( basis <= 394.39 )
							if( Upper_Band <= 398.696 )
								ret := -0.015957
							if( Upper_Band > 398.696 )
								ret := -0.389610
						if( basis > 394.39 )
							if( Lower_Band <= 393.762 )
								ret := 0.662162
							if( Lower_Band > 393.762 )
								ret := -0.384615
				if( bbm > 8.6306 )
					if( basis <= 283.165 )
						if( bearPower <= -15.0936 )
							if( Lower_Band <= 224.893 )
								ret := 0.932203 // buy
							if( Lower_Band > 224.893 )
								ret := 0.571429
						if( bearPower > -15.0936 )
							if( Lower_Band <= 199.002 )
								ret := 0.333333
							if( Lower_Band > 199.002 )
								ret := 0.729730 // buy
					if( basis > 283.165 )
						if( Lower_Band <= 297.145 )
							if( Lower_Band <= 287.372 )
								ret := -0.127660
							if( Lower_Band > 287.372 )
								ret := -0.828571 // sell
						if( Lower_Band > 297.145 )
							if( Lower_Band <= 315.352 )
								ret := 0.747475 // buy
							if( Lower_Band > 315.352 )
								ret := 0.168675
		if( bearPower > -4.94996 )
			if( basis <= 87.1299 )
				if( bearPower <= -1.23073 )
					if( bearPower <= -3.65692 )
						if( Lower_Band <= 82.25 )
							if( bullPower <= 0.083201 )
								ret := 0.699074
							if( bullPower > 0.083201 )
								ret := -0.090909
						if( Lower_Band > 82.25 )
							ret := -0.555556
					if( bearPower > -3.65692 )
						if( basis <= 56.5965 )
							if( bearPower <= -2.08169 )
								ret := 0.863636 // buy
							if( bearPower > -2.08169 )
								ret := 0.329787
						if( basis > 56.5965 )
							if( Upper_Band <= 80.965 )
								ret := 0.089413
							if( Upper_Band > 80.965 )
								ret := 0.256510
				if( bearPower > -1.23073 )
					if( bullPower <= 0.327505 )
						if( bbm <= 0.457386 )
							if( Upper_Band <= 41.255 )
								ret := -0.181996
							if( Upper_Band > 41.255 )
								ret := 0.008533
						if( bbm > 0.457386 )
							if( Lower_Band <= 54.0287 )
								ret := 0.168301
							if( Lower_Band > 54.0287 )
								ret := 0.053546
					if( bullPower > 0.327505 )
						if( Lower_Band <= 28.1687 )
							if( Upper_Band <= 33.846 )
								ret := 0.726415 // buy
							if( Upper_Band > 33.846 )
								ret := -0.625000
						if( Lower_Band > 28.1687 )
							if( bearPower <= 2.00898 )
								ret := 0.100838
							if( bearPower > 2.00898 )
								ret := -0.209125
			if( basis > 87.1299 )
				if( bearPower <= 7.16815 )
					if( Upper_Band <= 89.0684 )
						if( bearPower <= -1.71823 )
							if( Lower_Band <= 86.22 )
								ret := 0.636364
							if( Lower_Band > 86.22 )
								ret := 1.000000 // buy
						if( bearPower > -1.71823 )
							if( Upper_Band <= 87.9083 )
								ret := 0.727273 // buy
							if( Upper_Band > 87.9083 )
								ret := -0.274038
					if( Upper_Band > 89.0684 )
						if( bullPower <= 14.2351 )
							if( Lower_Band <= 388.318 )
								ret := 0.016914
							if( Lower_Band > 388.318 )
								ret := 0.269388
						if( bullPower > 14.2351 )
							if( bbp <= 21.971 )
								ret := 0.696970
							if( bbp > 21.971 )
								ret := -0.160000
				if( bearPower > 7.16815 )
					if( Upper_Band <= 387.711 )
						if( basis <= 181.259 )
							ret := -0.750000 // sell
						if( basis > 181.259 )
							if( basis <= 361.535 )
								ret := 0.548463
							if( basis > 361.535 )
								ret := -0.500000
					if( Upper_Band > 387.711 )
						if( bullPower <= 21.9276 )
							if( bullPower <= 14.373 )
								ret := -0.294118
							if( bullPower > 14.373 )
								ret := 0.531250
						if( bullPower > 21.9276 )
							if( Upper_Band <= 399.939 )
								ret := -0.600000
							if( Upper_Band > 399.939 )
								ret := -1.000000 // sell
	if( Upper_Band > 409.762 )
		if( Upper_Band <= 429.297 )
			if( bearPower <= -36.4446 )
				ret := 0.923077 // buy
			if( bearPower > -36.4446 )
				if( Upper_Band <= 412.417 )
					if( bearPower <= -9.03608 )
						if( Lower_Band <= 390.076 )
							if( bbp <= -17.6423 )
								ret := 0.600000
							if( bbp > -17.6423 )
								ret := -0.428571
						if( Lower_Band > 390.076 )
							if( bbm <= 9.48011 )
								ret := 1.000000 // buy
							if( bbm > 9.48011 )
								ret := 0.714286 // buy
					if( bearPower > -9.03608 )
						if( bearPower <= 4.99843 )
							if( basis <= 394.674 )
								ret := -0.571429
							if( basis > 394.674 )
								ret := -0.180124
						if( bearPower > 4.99843 )
							if( bbp <= 22.2739 )
								ret := 0.571429
							if( bbp > 22.2739 )
								ret := 0.285714
				if( Upper_Band > 412.417 )
					if( basis <= 403.016 )
						if( Lower_Band <= 378.985 )
							if( Lower_Band <= 373.804 )
								ret := -0.444444
							if( Lower_Band > 373.804 )
								ret := 0.103448
						if( Lower_Band > 378.985 )
							if( bullPower <= 10.769 )
								ret := -0.692661
							if( bullPower > 10.769 )
								ret := 0.066667
					if( basis > 403.016 )
						if( basis <= 408.903 )
							if( bbp <= 13.4032 )
								ret := -0.002959
							if( bbp > 13.4032 )
								ret := -0.611111
						if( basis > 408.903 )
							if( bullPower <= 1.36225 )
								ret := -0.176471
							if( bullPower > 1.36225 )
								ret := -0.538462
		if( Upper_Band > 429.297 )
			if( basis <= 424.786 )
				if( Upper_Band <= 474.821 )
					if( Lower_Band <= 394.211 )
						if( Lower_Band <= 332.362 )
							if( bbm <= 17.7819 )
								ret := 1.000000 // buy
							if( bbm > 17.7819 )
								ret := 0.750000 // buy
						if( Lower_Band > 332.362 )
							if( bearPower <= -19.369 )
								ret := 0.724138 // buy
							if( bearPower > -19.369 )
								ret := -0.093750
					if( Lower_Band > 394.211 )
						if( basis <= 415.164 )
							if( Lower_Band <= 396.35 )
								ret := 0.857143 // buy
							if( Lower_Band > 396.35 )
								ret := -0.571429
						if( basis > 415.164 )
							if( Lower_Band <= 400.297 )
								ret := 0.910256 // buy
							if( Lower_Band > 400.297 )
								ret := 0.605505
				if( Upper_Band > 474.821 )
					ret := -1.000000 // sell
			if( basis > 424.786 )
				if( Lower_Band <= 478.938 )
					if( Lower_Band <= 472.18 )
						if( Lower_Band <= 443.642 )
							if( basis <= 432.918 )
								ret := -0.365696
							if( basis > 432.918 )
								ret := 0.167331
						if( Lower_Band > 443.642 )
							if( bbp <= -27.0913 )
								ret := 0.789474 // buy
							if( bbp > -27.0913 )
								ret := -0.281671
					if( Lower_Band > 472.18 )
						if( bullPower <= 17.1683 )
							if( bearPower <= -14.62 )
								ret := 0.940000 // buy
							if( bearPower > -14.62 )
								ret := 0.563830
						if( bullPower > 17.1683 )
							if( bbm <= 13.5411 )
								ret := -0.692308
							if( bbm > 13.5411 )
								ret := 0.500000
				if( Lower_Band > 478.938 )
					if( basis <= 509.883 )
						if( basis <= 502.976 )
							if( bearPower <= -12.1874 )
								ret := 0.857143 // buy
							if( bearPower > -12.1874 )
								ret := -0.414286
						if( basis > 502.976 )
							if( basis <= 508.2 )
								ret := -0.933333 // sell
							if( basis > 508.2 )
								ret := -0.545455
					if( basis > 509.883 )
						if( basis <= 522.163 )
							if( basis <= 515.894 )
								ret := -0.258824
							if( basis > 515.894 )
								ret := 0.388489
						if( basis > 522.163 )
							if( bbp <= -56.5604 )
								ret := 0.590909
							if( bbp > -56.5604 )
								ret := -0.300485
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_AAVEUSDT_30Min_6cf4e1bd(Upper_Band, basis, Lower_Band, bullPower, bbp, bearPower, bbm, BBPower_Color)

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



//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bollinger_Bands, L_Bull_Bear_Power
// ID_model: NVST_5Min_2BB0_e78b6489 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_NVST_5Min_2BB0_e78b6489", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_NVST_5Min_e78b6489(basis, Upper_Band, Lower_Band, bearPower, bbm, bbp, bullPower, BBPower_Color)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( basis <= 35.2334 )
		if( basis <= 16.3346 )
			if( Upper_Band <= 16.3941 )
				if( basis <= 14.8837 )
					if( bbp <= -0.026721 )
						ret := 0.750000 // buy
					if( bbp > -0.026721 )
						ret := 1.000000 // buy
				if( basis > 14.8837 )
					if( Upper_Band <= 15.6767 )
						if( Upper_Band <= 15.6643 )
							ret := -1.000000 // sell
						if( Upper_Band > 15.6643 )
							ret := -0.588235
					if( Upper_Band > 15.6767 )
						if( basis <= 15.913 )
							ret := 0.404682
						if( basis > 15.913 )
							ret := 0.019591
			if( Upper_Band > 16.3941 )
				if( bbp <= 0.275407 )
					if( basis <= 16.3091 )
						if( Upper_Band <= 16.857 )
							ret := 0.664653
						if( Upper_Band > 16.857 )
							ret := -0.040000
					if( basis > 16.3091 )
						if( bbm <= 0.09507 )
							ret := 0.384615
						if( bbm > 0.09507 )
							ret := -0.764706 // sell
				if( bbp > 0.275407 )
					if( Lower_Band <= 15.6538 )
						ret := -0.647059
					if( Lower_Band > 15.6538 )
						if( basis <= 16.2541 )
							ret := -1.000000 // sell
						if( basis > 16.2541 )
							ret := -0.875000 // sell
		if( basis > 16.3346 )
			if( bbp <= -1.15293 )
				if( basis <= 33.1688 )
					if( bearPower <= -0.887384 )
						ret := 1.000000 // buy
					if( bearPower > -0.887384 )
						if( bbp <= -1.40875 )
							ret := 0.200000
						if( bbp > -1.40875 )
							ret := 1.000000 // buy
				if( basis > 33.1688 )
					ret := 0.300000
			if( bbp > -1.15293 )
				if( bbm <= 0.193601 )
					if( Lower_Band <= 16.4397 )
						if( basis <= 16.4477 )
							ret := 0.013575
						if( basis > 16.4477 )
							ret := -0.461538
					if( Lower_Band > 16.4397 )
						if( Upper_Band <= 17.3115 )
							ret := 0.206204
						if( Upper_Band > 17.3115 )
							ret := -0.001643
				if( bbm > 0.193601 )
					if( Lower_Band <= 34.9091 )
						if( Lower_Band <= 23.7141 )
							ret := -0.046358
						if( Lower_Band > 23.7141 )
							ret := -0.331715
					if( Lower_Band > 34.9091 )
						if( bearPower <= -0.117692 )
							ret := 0.916667 // buy
						if( bearPower > -0.117692 )
							ret := 0.545455
	if( basis > 35.2334 )
		if( Upper_Band <= 36.5614 )
			if( Upper_Band <= 35.5566 )
				if( bbp <= -0.137087 )
					if( bbm <= 0.066771 )
						ret := 0.894737 // buy
					if( bbm > 0.066771 )
						ret := 0.375000
				if( bbp > -0.137087 )
					if( Upper_Band <= 35.5244 )
						if( bullPower <= -0.028802 )
							ret := -1.000000 // sell
						if( bullPower > -0.028802 )
							ret := -0.159091
					if( Upper_Band > 35.5244 )
						if( basis <= 35.3228 )
							ret := 0.761905 // buy
						if( basis > 35.3228 )
							ret := 0.066667
			if( Upper_Band > 35.5566 )
				if( Lower_Band <= 35.4844 )
					if( basis <= 35.6944 )
						if( Lower_Band <= 35.0332 )
							ret := -0.825397 // sell
						if( Lower_Band > 35.0332 )
							ret := -0.449814
					if( basis > 35.6944 )
						if( basis <= 35.742 )
							ret := -1.000000 // sell
						if( basis > 35.742 )
							ret := -0.444444
				if( Lower_Band > 35.4844 )
					if( Lower_Band <= 35.6033 )
						if( bbm <= 0.044676 )
							ret := -0.250000
						if( bbm > 0.044676 )
							ret := 0.186047
					if( Lower_Band > 35.6033 )
						ret := -0.812500 // sell
		if( Upper_Band > 36.5614 )
			if( basis <= 37.8317 )
				if( Lower_Band <= 37.3294 )
					if( bullPower <= -0.169044 )
						if( bearPower <= -0.934435 )
							ret := 0.600000
						if( bearPower > -0.934435 )
							ret := 1.000000 // buy
					if( bullPower > -0.169044 )
						if( bbm <= 0.198807 )
							ret := 0.138462
						if( bbm > 0.198807 )
							ret := -0.900000 // sell
				if( Lower_Band > 37.3294 )
					if( bbm <= 0.040751 )
						ret := 0.000000
					if( bbm > 0.040751 )
						if( basis <= 37.7983 )
							ret := 0.883721 // buy
						if( basis > 37.7983 )
							ret := 0.217391
			if( basis > 37.8317 )
				if( Lower_Band <= 37.655 )
					if( bearPower <= -0.153039 )
						if( bullPower <= -0.118429 )
							ret := -0.809524 // sell
						if( bullPower > -0.118429 )
							ret := -1.000000 // sell
					if( bearPower > -0.153039 )
						if( basis <= 37.8778 )
							ret := -0.727273 // sell
						if( basis > 37.8778 )
							ret := 0.000000
				if( Lower_Band > 37.655 )
					if( Upper_Band <= 39.2717 )
						if( bbm <= 0.140217 )
							ret := -0.044665
						if( bbm > 0.140217 )
							ret := -0.612903
					if( Upper_Band > 39.2717 )
						if( bullPower <= 0.033728 )
							ret := -0.187500
						if( bullPower > 0.033728 )
							ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
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
float op_operation = decision_tree_0_NVST_5Min_e78b6489(basis, Upper_Band, Lower_Band, bearPower, bbm, bbp, bullPower, BBPower_Color)

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



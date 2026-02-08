//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bollinger_Bands, L_Bull_Bear_Power
// ID_model: ABNB_30Min_2BB0_b96f3d5e Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ABNB_30Min_2BB0_b96f3d5e", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ABNB_30Min_b96f3d5e(Upper_Band, basis, Lower_Band, bullPower, bbp, bearPower, bbm, BBPower_Color)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( Lower_Band <= 167.551 )
		if( basis <= 116.539 )
			if( bullPower <= 0.511912 )
				if( Lower_Band <= 112.068 )
					if( basis <= 114.037 )
						if( Lower_Band <= 110.904 )
							ret := -0.013955
						if( Lower_Band > 110.904 )
							ret := 0.384181
					if( basis > 114.037 )
						if( Upper_Band <= 120.762 )
							ret := -0.586667
						if( Upper_Band > 120.762 )
							ret := 0.941176 // buy
				if( Lower_Band > 112.068 )
					if( bearPower <= 0.154437 )
						if( Lower_Band <= 115.166 )
							ret := 0.285363
						if( Lower_Band > 115.166 )
							ret := 0.775862 // buy
					if( bearPower > 0.154437 )
						if( bbp <= 0.624485 )
							ret := 0.069767
						if( bbp > 0.624485 )
							ret := -0.545455
			if( bullPower > 0.511912 )
				if( Upper_Band <= 100.579 )
					if( bbm <= 0.012489 )
						if( Upper_Band <= 87.3131 )
							ret := -1.000000 // sell
						if( Upper_Band > 87.3131 )
							ret := 0.187500
					if( bbm > 0.012489 )
						if( basis <= 95.1586 )
							ret := 0.525591
						if( basis > 95.1586 )
							ret := 0.314815
				if( Upper_Band > 100.579 )
					if( basis <= 101.11 )
						if( Lower_Band <= 98.3956 )
							ret := -0.049296
						if( Lower_Band > 98.3956 )
							ret := -0.548077
					if( basis > 101.11 )
						if( bbm <= 0.273952 )
							ret := -0.159639
						if( bbm > 0.273952 )
							ret := 0.192990
		if( basis > 116.539 )
			if( basis <= 131.976 )
				if( Lower_Band <= 130.423 )
					if( Upper_Band <= 135.67 )
						if( basis <= 127.579 )
							ret := -0.020807
						if( basis > 127.579 )
							ret := -0.200889
					if( Upper_Band > 135.67 )
						if( bearPower <= -1.02041 )
							ret := -0.887500 // sell
						if( bearPower > -1.02041 )
							ret := -0.238095
				if( Lower_Band > 130.423 )
					if( basis <= 131.836 )
						if( bbp <= 0.063054 )
							ret := -0.983871 // sell
						if( bbp > 0.063054 )
							ret := -0.625000
					if( basis > 131.836 )
						ret := -0.071429
			if( basis > 131.976 )
				if( Lower_Band <= 132.021 )
					if( Upper_Band <= 137.736 )
						if( BBPower_Color <= 0.5 )
							ret := 0.618677
						if( BBPower_Color > 0.5 )
							ret := 0.125424
					if( Upper_Band > 137.736 )
						if( bbp <= 5.06599 )
							ret := 0.036184
						if( bbp > 5.06599 )
							ret := -0.941176 // sell
				if( Lower_Band > 132.021 )
					if( basis <= 159.722 )
						if( Upper_Band <= 160.902 )
							ret := -0.008222
						if( Upper_Band > 160.902 )
							ret := -0.257340
					if( basis > 159.722 )
						if( basis <= 163.303 )
							ret := 0.229374
						if( basis > 163.303 )
							ret := 0.011978
	if( Lower_Band > 167.551 )
		if( basis <= 206.828 )
			if( bbm <= 0.49995 )
				if( Upper_Band <= 176.284 )
					if( Lower_Band <= 168.6 )
						if( bullPower <= 0.394554 )
							ret := 0.580247
						if( bullPower > 0.394554 )
							ret := -0.366667
					if( Lower_Band > 168.6 )
						if( bbm <= 0.364093 )
							ret := -0.371859
						if( bbm > 0.364093 )
							ret := 0.220000
				if( Upper_Band > 176.284 )
					if( Lower_Band <= 191.237 )
						if( bullPower <= 0.74046 )
							ret := 0.352000
						if( bullPower > 0.74046 )
							ret := -0.086331
					if( Lower_Band > 191.237 )
						if( bullPower <= 1.20571 )
							ret := -0.316129
						if( bullPower > 1.20571 )
							ret := 0.229167
			if( bbm > 0.49995 )
				if( Lower_Band <= 201.913 )
					if( bullPower <= -1.50592 )
						if( Lower_Band <= 185.942 )
							ret := 0.316239
						if( Lower_Band > 185.942 )
							ret := -0.223022
					if( bullPower > -1.50592 )
						if( Lower_Band <= 168.187 )
							ret := -0.530303
						if( Lower_Band > 168.187 )
							ret := -0.183918
				if( Lower_Band > 201.913 )
					if( Lower_Band <= 203.263 )
						if( Upper_Band <= 207.636 )
							ret := 0.000000
						if( Upper_Band > 207.636 )
							ret := 0.976190 // buy
					if( Lower_Band > 203.263 )
						if( bullPower <= 2.65227 )
							ret := -0.083333
						if( bullPower > 2.65227 )
							ret := -1.000000 // sell
		if( basis > 206.828 )
			if( basis <= 210.809 )
				if( bearPower <= -1.74204 )
					if( Lower_Band <= 198.927 )
						ret := 1.000000 // buy
					if( Lower_Band > 198.927 )
						if( bearPower <= -6.21945 )
							ret := -0.200000
						if( bearPower > -6.21945 )
							ret := -0.976190 // sell
				if( bearPower > -1.74204 )
					if( basis <= 208.781 )
						if( bullPower <= 0.126866 )
							ret := -0.437500
						if( bullPower > 0.126866 )
							ret := -0.891892 // sell
					if( basis > 208.781 )
						if( basis <= 210.096 )
							ret := -0.142857
						if( basis > 210.096 )
							ret := -0.909091 // sell
			if( basis > 210.809 )
				if( bullPower <= 2.24178 )
					if( basis <= 214.03 )
						if( bbm <= 0.723213 )
							ret := 0.117647
						if( bbm > 0.723213 )
							ret := 0.756098 // buy
					if( basis > 214.03 )
						if( bbm <= 2.67927 )
							ret := -0.416667
						if( bbm > 2.67927 )
							ret := 0.909091 // buy
				if( bullPower > 2.24178 )
					if( bullPower <= 5.44083 )
						if( Upper_Band <= 219.01 )
							ret := -1.000000 // sell
						if( Upper_Band > 219.01 )
							ret := 0.000000
					if( bullPower > 5.44083 )
						ret := 1.000000 // buy
	
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
float op_operation = decision_tree_0_ABNB_30Min_b96f3d5e(Upper_Band, basis, Lower_Band, bullPower, bbp, bearPower, bbm, BBPower_Color)

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



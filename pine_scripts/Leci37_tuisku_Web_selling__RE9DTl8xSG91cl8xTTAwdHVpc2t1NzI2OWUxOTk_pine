//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index
// ID_model: DOCN_1Hour_1M00_7269e199 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DOCN_1Hour_1M00_7269e199", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DOCN_1Hour_7269e199(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( Positive_Money_Flow <= 56.5345 )
		if( Money_Flow_Ratio <= 2.18762 )
			if( Typical_Price <= 90.2585 )
				if( Positive_Money_Flow_Sum <= 5.81566e+06 )
					if( Negative_Money_Flow <= 1.31974e+06 )
						if( MFI_High <= -65.2361 )
							ret := -0.074074
						if( MFI_High > -65.2361 )
							ret := -0.800000 // sell
					if( Negative_Money_Flow > 1.31974e+06 )
						if( Typical_Price <= 40.7493 )
							ret := 0.260274
						if( Typical_Price > 40.7493 )
							ret := -0.700000 // sell
				if( Positive_Money_Flow_Sum > 5.81566e+06 )
					if( Negative_Money_Flow_Sum <= 1.75456e+08 )
						if( Negative_Money_Flow_Sum <= 7.91331e+07 )
							ret := 0.091736
						if( Negative_Money_Flow_Sum > 7.91331e+07 )
							ret := -0.084022
					if( Negative_Money_Flow_Sum > 1.75456e+08 )
						if( Negative_Money_Flow <= 150781 )
							ret := -0.320000
						if( Negative_Money_Flow > 150781 )
							ret := 0.489051
			if( Typical_Price > 90.2585 )
				if( Positive_Money_Flow_Sum <= 2.76108e+08 )
					if( Positive_Money_Flow_Sum <= 1.6216e+08 )
						if( Positive_Money_Flow_Sum <= 7.84251e+07 )
							ret := -0.067568
						if( Positive_Money_Flow_Sum > 7.84251e+07 )
							ret := -0.484375
					if( Positive_Money_Flow_Sum > 1.6216e+08 )
						ret := 0.888889 // buy
				if( Positive_Money_Flow_Sum > 2.76108e+08 )
					if( Negative_Money_Flow_Sum <= 2.73544e+08 )
						if( Typical_Price <= 113.542 )
							ret := -1.000000 // sell
						if( Typical_Price > 113.542 )
							ret := 0.000000
					if( Negative_Money_Flow_Sum > 2.73544e+08 )
						ret := 0.000000
		if( Money_Flow_Ratio > 2.18762 )
			if( Positive_Money_Flow_Sum <= 1.26555e+08 )
				if( Negative_Money_Flow_Sum <= 1.46066e+07 )
					if( Typical_Price <= 36.895 )
						if( Negative_Money_Flow <= 214135 )
							ret := 0.152778
						if( Negative_Money_Flow > 214135 )
							ret := -0.277778
					if( Typical_Price > 36.895 )
						if( Typical_Price <= 54.3108 )
							ret := 0.310345
						if( Typical_Price > 54.3108 )
							ret := -0.650000
				if( Negative_Money_Flow_Sum > 1.46066e+07 )
					if( Positive_Money_Flow_Sum <= 6.65077e+07 )
						if( Positive_Money_Flow_Sum <= 6.4027e+07 )
							ret := 0.505435
						if( Positive_Money_Flow_Sum > 6.4027e+07 )
							ret := -1.000000 // sell
					if( Positive_Money_Flow_Sum > 6.65077e+07 )
						if( MFI_High <= -11.4679 )
							ret := -1.000000 // sell
						if( MFI_High > -11.4679 )
							ret := 0.704762 // buy
			if( Positive_Money_Flow_Sum > 1.26555e+08 )
				if( Typical_Price <= 43.3598 )
					if( Positive_Money_Flow_Sum <= 1.27062e+08 )
						ret := -1.000000 // sell
					if( Positive_Money_Flow_Sum > 1.27062e+08 )
						if( Typical_Price <= 36.84 )
							ret := 0.000000
						if( Typical_Price > 36.84 )
							ret := -0.533333
				if( Typical_Price > 43.3598 )
					if( Negative_Money_Flow <= 243391 )
						if( MFI <= 73.6337 )
							ret := -0.739130 // sell
						if( MFI > 73.6337 )
							ret := 0.000000
					if( Negative_Money_Flow > 243391 )
						if( Negative_Money_Flow_Sum <= 4.57878e+07 )
							ret := -0.257143
						if( Negative_Money_Flow_Sum > 4.57878e+07 )
							ret := 0.514286
	if( Positive_Money_Flow > 56.5345 )
		if( Negative_Money_Flow_Sum <= 1.15313e+07 )
			if( Positive_Money_Flow <= 50293.1 )
				if( Typical_Price <= 45.5083 )
					if( MFI <= 57.2773 )
						if( Positive_Money_Flow <= 38685.6 )
							ret := -1.000000 // sell
						if( Positive_Money_Flow > 38685.6 )
							ret := 0.000000
					if( MFI > 57.2773 )
						if( Negative_Money_Flow <= 2794.76 )
							ret := -0.430000
						if( Negative_Money_Flow > 2794.76 )
							ret := 0.029412
				if( Typical_Price > 45.5083 )
					if( Typical_Price <= 48.9612 )
						ret := 0.937500 // buy
					if( Typical_Price > 48.9612 )
						if( Raw_Money_Flow <= 19281.9 )
							ret := 0.666667
						if( Raw_Money_Flow > 19281.9 )
							ret := -0.375000
			if( Positive_Money_Flow > 50293.1 )
				if( Typical_Price <= 41.1423 )
					if( Positive_Money_Flow_Sum <= 1.80971e+07 )
						if( Negative_Money_Flow <= 1.10345e+06 )
							ret := 0.761194 // buy
						if( Negative_Money_Flow > 1.10345e+06 )
							ret := -0.333333
					if( Positive_Money_Flow_Sum > 1.80971e+07 )
						if( Typical_Price <= 29.1661 )
							ret := -0.088608
						if( Typical_Price > 29.1661 )
							ret := 0.358839
				if( Typical_Price > 41.1423 )
					if( Negative_Money_Flow_Sum <= 5.16523e+06 )
						if( Positive_Money_Flow_Sum <= 1.77179e+08 )
							ret := 0.096774
						if( Positive_Money_Flow_Sum > 1.77179e+08 )
							ret := 0.656250
					if( Negative_Money_Flow_Sum > 5.16523e+06 )
						if( Positive_Money_Flow_Sum <= 2.14945e+07 )
							ret := 0.196429
						if( Positive_Money_Flow_Sum > 2.14945e+07 )
							ret := -0.345133
		if( Negative_Money_Flow_Sum > 1.15313e+07 )
			if( Typical_Price <= 32.9345 )
				if( Typical_Price <= 26.4705 )
					if( Positive_Money_Flow <= 2381 )
						ret := -1.000000 // sell
					if( Positive_Money_Flow > 2381 )
						if( MFI_Low <= 35.9239 )
							ret := -0.011364
						if( MFI_Low > 35.9239 )
							ret := -0.400000
				if( Typical_Price > 26.4705 )
					if( Positive_Money_Flow_Sum <= 1.09732e+07 )
						if( Raw_Money_Flow <= 1.8093e+06 )
							ret := 0.323529
						if( Raw_Money_Flow > 1.8093e+06 )
							ret := 0.833333 // buy
					if( Positive_Money_Flow_Sum > 1.09732e+07 )
						if( MFI_Low <= 36.5093 )
							ret := -0.036946
						if( MFI_Low > 36.5093 )
							ret := 0.225627
			if( Typical_Price > 32.9345 )
				if( Negative_Money_Flow <= 179999 )
					if( Positive_Money_Flow_Sum <= 3.06403e+07 )
						if( MFI_High <= -67.3989 )
							ret := 0.261261
						if( MFI_High > -67.3989 )
							ret := -0.241835
					if( Positive_Money_Flow_Sum > 3.06403e+07 )
						if( Typical_Price <= 63.0228 )
							ret := -0.082004
						if( Typical_Price > 63.0228 )
							ret := 0.053961
				if( Negative_Money_Flow > 179999 )
					if( Negative_Money_Flow_Sum <= 1.74786e+08 )
						if( MFI_Low <= 48.104 )
							ret := -0.482353
						if( MFI_Low > 48.104 )
							ret := 0.000000
					if( Negative_Money_Flow_Sum > 1.74786e+08 )
						if( Raw_Money_Flow <= 1.38855e+07 )
							ret := 0.750000 // buy
						if( Raw_Money_Flow > 1.38855e+07 )
							ret := -0.142857
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
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
float op_operation = decision_tree_0_DOCN_1Hour_7269e199(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)

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



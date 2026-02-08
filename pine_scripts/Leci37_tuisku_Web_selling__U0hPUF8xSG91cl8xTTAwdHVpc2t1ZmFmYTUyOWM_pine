//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index
// ID_model: SHOP_1Hour_1M00_fafa529c Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SHOP_1Hour_1M00_fafa529c", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SHOP_1Hour_fafa529c(Negative_Money_Flow_Sum, MFI_High, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, Typical_Price, MFI, Positive_Money_Flow_Sum, Positive_Money_Flow)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( Negative_Money_Flow_Sum <= 8.57037e+08 )
		if( Raw_Money_Flow <= 7.97544e+06 )
			if( Typical_Price <= 91.5615 )
				if( Negative_Money_Flow_Sum <= 6.6562e+08 )
					if( Typical_Price <= 32.2294 )
						if( MFI_Low <= 11.3558 )
							ret := 0.784091 // buy
						if( MFI_Low > 11.3558 )
							ret := 0.206478
					if( Typical_Price > 32.2294 )
						if( MFI_Low <= 23.2886 )
							ret := 0.107943
						if( MFI_Low > 23.2886 )
							ret := -0.061317
				if( Negative_Money_Flow_Sum > 6.6562e+08 )
					if( Negative_Money_Flow_Sum <= 8.28844e+08 )
						if( Typical_Price <= 35.1182 )
							ret := -0.583333
						if( Typical_Price > 35.1182 )
							ret := -0.300000
					if( Negative_Money_Flow_Sum > 8.28844e+08 )
						if( Raw_Money_Flow <= 1.70541e+06 )
							ret := 0.236842
						if( Raw_Money_Flow > 1.70541e+06 )
							ret := 0.900000 // buy
			if( Typical_Price > 91.5615 )
				if( MFI_Low <= 65.9475 )
					if( Positive_Money_Flow_Sum <= 3.78066e+07 )
						if( Typical_Price <= 128.523 )
							ret := 1.000000 // buy
						if( Typical_Price > 128.523 )
							ret := 0.636364
					if( Positive_Money_Flow_Sum > 3.78066e+07 )
						if( MFI_High <= -63.7356 )
							ret := -0.234568
						if( MFI_High > -63.7356 )
							ret := 0.204775
				if( MFI_Low > 65.9475 )
					if( Positive_Money_Flow_Sum <= 2.18062e+09 )
						if( Negative_Money_Flow_Sum <= 1.83372e+08 )
							ret := -0.072368
						if( Negative_Money_Flow_Sum > 1.83372e+08 )
							ret := -0.815789 // sell
					if( Positive_Money_Flow_Sum > 2.18062e+09 )
						if( Typical_Price <= 1024.23 )
							ret := 0.600000
						if( Typical_Price > 1024.23 )
							ret := -0.322581
		if( Raw_Money_Flow > 7.97544e+06 )
			if( Money_Flow_Ratio <= 3.52315 )
				if( Positive_Money_Flow_Sum <= 1.01721e+08 )
					if( Negative_Money_Flow <= 8.26668e+07 )
						if( Typical_Price <= 61.0946 )
							ret := -0.389140
						if( Typical_Price > 61.0946 )
							ret := 0.237143
					if( Negative_Money_Flow > 8.26668e+07 )
						if( Positive_Money_Flow_Sum <= 948035 )
							ret := -0.700000 // sell
						if( Positive_Money_Flow_Sum > 948035 )
							ret := 0.444867
				if( Positive_Money_Flow_Sum > 1.01721e+08 )
					if( Positive_Money_Flow <= 1.9153e+07 )
						if( Negative_Money_Flow_Sum <= 8.41259e+07 )
							ret := 0.309735
						if( Negative_Money_Flow_Sum > 8.41259e+07 )
							ret := -0.092102
					if( Positive_Money_Flow > 1.9153e+07 )
						if( Money_Flow_Ratio <= 3.15781 )
							ret := 0.024494
						if( Money_Flow_Ratio > 3.15781 )
							ret := -0.271277
			if( Money_Flow_Ratio > 3.52315 )
				if( Positive_Money_Flow_Sum <= 2.55291e+08 )
					if( Positive_Money_Flow_Sum <= 1.66576e+08 )
						if( Negative_Money_Flow_Sum <= 2.6198e+07 )
							ret := 0.000000
						if( Negative_Money_Flow_Sum > 2.6198e+07 )
							ret := 1.000000 // buy
					if( Positive_Money_Flow_Sum > 1.66576e+08 )
						if( Positive_Money_Flow_Sum <= 2.52694e+08 )
							ret := 0.392157
						if( Positive_Money_Flow_Sum > 2.52694e+08 )
							ret := 0.916667 // buy
				if( Positive_Money_Flow_Sum > 2.55291e+08 )
					if( Positive_Money_Flow_Sum <= 1.25873e+09 )
						if( Typical_Price <= 78.5775 )
							ret := 0.121988
						if( Typical_Price > 78.5775 )
							ret := -0.176110
					if( Positive_Money_Flow_Sum > 1.25873e+09 )
						if( Positive_Money_Flow <= 2.72496e+08 )
							ret := 0.320273
						if( Positive_Money_Flow > 2.72496e+08 )
							ret := -0.006689
	if( Negative_Money_Flow_Sum > 8.57037e+08 )
		if( MFI_High <= -76.4976 )
			if( Negative_Money_Flow <= 7.04385e+08 )
				if( Typical_Price <= 59.0831 )
					if( Typical_Price <= 40.7256 )
						ret := 0.888889 // buy
					if( Typical_Price > 40.7256 )
						if( MFI <= 2.41234 )
							ret := 0.250000
						if( MFI > 2.41234 )
							ret := -1.000000 // sell
				if( Typical_Price > 59.0831 )
					if( Negative_Money_Flow_Sum <= 1.61888e+09 )
						if( MFI_High <= -79.7676 )
							ret := -0.594595
						if( MFI_High > -79.7676 )
							ret := -0.871212 // sell
					if( Negative_Money_Flow_Sum > 1.61888e+09 )
						if( Negative_Money_Flow_Sum <= 2.03918e+09 )
							ret := 0.322222
						if( Negative_Money_Flow_Sum > 2.03918e+09 )
							ret := -0.631579
			if( Negative_Money_Flow > 7.04385e+08 )
				ret := 1.000000 // buy
		if( MFI_High > -76.4976 )
			if( Negative_Money_Flow <= 187115 )
				if( Typical_Price <= 368.451 )
					if( MFI_Low <= 31.9698 )
						if( Negative_Money_Flow_Sum <= 1.14541e+09 )
							ret := -0.244186
						if( Negative_Money_Flow_Sum > 1.14541e+09 )
							ret := 0.313953
					if( MFI_Low > 31.9698 )
						if( Negative_Money_Flow_Sum <= 9.42903e+08 )
							ret := 1.000000 // buy
						if( Negative_Money_Flow_Sum > 9.42903e+08 )
							ret := 0.250000
				if( Typical_Price > 368.451 )
					if( MFI <= 25.2842 )
						if( Positive_Money_Flow <= 2.06072e+06 )
							ret := -0.612245
						if( Positive_Money_Flow > 2.06072e+06 )
							ret := -0.269565
					if( MFI > 25.2842 )
						if( Typical_Price <= 501.855 )
							ret := -0.448864
						if( Typical_Price > 501.855 )
							ret := -0.156814
			if( Negative_Money_Flow > 187115 )
				if( Positive_Money_Flow_Sum <= 5.05827e+08 )
					if( Negative_Money_Flow <= 372923 )
						if( Typical_Price <= 1117.44 )
							ret := 0.839286 // buy
						if( Typical_Price > 1117.44 )
							ret := -0.416667
					if( Negative_Money_Flow > 372923 )
						if( Negative_Money_Flow_Sum <= 2.04539e+09 )
							ret := -0.074672
						if( Negative_Money_Flow_Sum > 2.04539e+09 )
							ret := 0.284153
				if( Positive_Money_Flow_Sum > 5.05827e+08 )
					if( Positive_Money_Flow_Sum <= 1.34654e+09 )
						if( Negative_Money_Flow <= 3.6733e+08 )
							ret := -0.231586
						if( Negative_Money_Flow > 3.6733e+08 )
							ret := 0.168067
					if( Positive_Money_Flow_Sum > 1.34654e+09 )
						if( Raw_Money_Flow <= 2.26151e+08 )
							ret := 0.282051
						if( Raw_Money_Flow > 2.26151e+08 )
							ret := -0.295820
	
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
float op_operation = decision_tree_0_SHOP_1Hour_fafa529c(Negative_Money_Flow_Sum, MFI_High, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Money_Flow_Ratio, Typical_Price, MFI, Positive_Money_Flow_Sum, Positive_Money_Flow)

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



//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_MA_Cross_SMA, L_Money_Flow_Index
// ID_model: NVDA_1Day_2MM0_54f83cff Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_NVDA_1Day_2MM0_54f83cff", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_NVDA_1Day_54f83cff(Short_MA, Long_MA, Short_Long_Diff, MA_Cross, Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=5, max_features=0.65, max_leaf_nodes=30,random_state=843828734)
	if( Raw_Money_Flow <= 8.42846e+09 )
		if( Long_MA <= 161.672 )
			if( Raw_Money_Flow <= 5.95954e+09 )
				if( Money_Flow_Ratio <= 2.54295 )
					if( Negative_Money_Flow <= 4.03447e+09 )
						ret := 0.328194
					if( Negative_Money_Flow > 4.03447e+09 )
						ret := -0.625000
				if( Money_Flow_Ratio > 2.54295 )
					if( Typical_Price <= 108.105 )
						ret := 0.129630
					if( Typical_Price > 108.105 )
						ret := -0.388889
			if( Raw_Money_Flow > 5.95954e+09 )
				if( Positive_Money_Flow <= 7.96162e+09 )
					if( Short_Long_Diff <= 12.3105 )
						ret := 0.864078 // buy
					if( Short_Long_Diff > 12.3105 )
						ret := 0.000000
				if( Positive_Money_Flow > 7.96162e+09 )
					if( Raw_Money_Flow <= 8.03468e+09 )
						ret := -1.000000 // sell
					if( Raw_Money_Flow > 8.03468e+09 )
						ret := 0.600000
		if( Long_MA > 161.672 )
			if( Long_MA <= 277.938 )
				if( MFI_Low <= 55.485 )
					if( Negative_Money_Flow_Sum <= 4.66046e+10 )
						ret := -0.129702
					if( Negative_Money_Flow_Sum > 4.66046e+10 )
						ret := -0.654867
				if( MFI_Low > 55.485 )
					if( Positive_Money_Flow_Sum <= 4.28694e+10 )
						ret := 0.043478
					if( Positive_Money_Flow_Sum > 4.28694e+10 )
						ret := 0.883721 // buy
			if( Long_MA > 277.938 )
				if( Short_MA <= 548.32 )
					if( Positive_Money_Flow_Sum <= 4.04415e+10 )
						ret := 0.597510
					if( Positive_Money_Flow_Sum > 4.04415e+10 )
						ret := 0.070000
				if( Short_MA > 548.32 )
					if( Positive_Money_Flow <= 1.98765e+07 )
						ret := 0.264706
					if( Positive_Money_Flow > 1.98765e+07 )
						ret := -0.637931
	if( Raw_Money_Flow > 8.42846e+09 )
		if( Negative_Money_Flow_Sum <= 3.54112e+11 )
			if( Short_Long_Diff <= 35.1307 )
				if( Long_MA <= 399.573 )
					if( Short_MA <= 123.482 )
						ret := 0.340000
					if( Short_MA > 123.482 )
						ret := -0.394102
				if( Long_MA > 399.573 )
					if( Long_MA <= 734.413 )
						ret := 0.141631
					if( Long_MA > 734.413 )
						ret := -0.724138 // sell
			if( Short_Long_Diff > 35.1307 )
				if( MFI <= 76.7086 )
					if( Short_Long_Diff <= 49.0021 )
						ret := 0.782609 // buy
					if( Short_Long_Diff > 49.0021 )
						ret := -0.181818
				if( MFI > 76.7086 )
					if( MFI_High <= 1.124 )
						ret := -0.937500 // sell
					if( MFI_High > 1.124 )
						ret := 0.000000
		if( Negative_Money_Flow_Sum > 3.54112e+11 )
			if( Short_Long_Diff <= -0.836349 )
				if( Money_Flow_Ratio <= 0.742334 )
					if( Positive_Money_Flow <= 3.44358e+10 )
						ret := 0.968254 // buy
					if( Positive_Money_Flow > 3.44358e+10 )
						ret := 0.000000
				if( Money_Flow_Ratio > 0.742334 )
					ret := 0.000000
			if( Short_Long_Diff > -0.836349 )
				if( Negative_Money_Flow_Sum <= 3.57502e+11 )
					ret := 1.000000 // buy
				if( Negative_Money_Flow_Sum > 3.57502e+11 )
					ret := 0.000000
	
    ret //return
// Define expected timeframe based on the selected interval: 1Day pine_value: D   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1DAY !!"
if (str.tostring(timeframe.period) != "D")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_MA_Cross_SMA 
//@version=5
//indicator title="MA Cross", overlay=true)

shortlen = input.int(9, title="Short MA Length", minval=1)
longlen = input.int(21, title="Long MA Length", minval=1)

// Calculate the short and long simple moving averages (SMA)
Short_MA = ta.sma(close, shortlen)
Long_MA = ta.sma(close, longlen)

// Calculate the difference between short MA and long MA
Short_Long_Diff = Short_MA - Long_MA

// Identify crossover points where short MA crosses above or below the long MA
MA_Cross = ta.valuewhen(ta.crossover(Short_MA, Long_MA), Short_MA, 0)

// Plot the results
plot(Short_MA, color=color.orange, title="Short MA")
plot(Long_MA, color=color.green, title="Long MA")
plotshape(na(MA_Cross) ? na : MA_Cross, style=shape.cross, location=location.absolute, color=color.blue, title="Cross")


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
float op_operation = decision_tree_0_NVDA_1Day_54f83cff(Short_MA, Long_MA, Short_Long_Diff, MA_Cross, Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)

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



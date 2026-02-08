//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Stochastic_RSI
// ID_model: TWLO_30Min_2MS0_6e53b79c Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_TWLO_30Min_2MS0_6e53b79c", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_TWLO_30Min_6e53b79c(Typical_Price, MFI_High, Negative_Money_Flow, Positive_Money_Flow, Money_Flow_Ratio, MFI, Negative_Money_Flow_Sum, Positive_Money_Flow_Sum, MFI_Low, Raw_Money_Flow, rsi1, d, k, smoothD_d, d_k, smoothK_k)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( d_k <= -1.16466 )
		if( Positive_Money_Flow <= 3465.65 )
			if( Raw_Money_Flow <= 553825 )
				if( k <= 37.4474 )
					if( rsi1 <= 50.0312 )
						if( d <= 27.0535 )
							ret := 0.275418
						if( d > 27.0535 )
							ret := 0.742424 // buy
					if( rsi1 > 50.0312 )
						if( k <= 18.9092 )
							ret := -0.500000
						if( k > 18.9092 )
							ret := 0.123377
				if( k > 37.4474 )
					if( rsi1 <= 83.6192 )
						if( Typical_Price <= 269.022 )
							ret := -0.002679
						if( Typical_Price > 269.022 )
							ret := 0.311404
					if( rsi1 > 83.6192 )
						if( Positive_Money_Flow_Sum <= 9.53738e+07 )
							ret := 0.062500
						if( Positive_Money_Flow_Sum > 9.53738e+07 )
							ret := 0.783784 // buy
			if( Raw_Money_Flow > 553825 )
				if( Raw_Money_Flow <= 957332 )
					if( d_k <= -5.02084 )
						if( MFI_High <= -11.6924 )
							ret := 0.027972
						if( MFI_High > -11.6924 )
							ret := -0.750000 // sell
					if( d_k > -5.02084 )
						if( Negative_Money_Flow_Sum <= 5.47721e+06 )
							ret := -0.823529 // sell
						if( Negative_Money_Flow_Sum > 5.47721e+06 )
							ret := -0.330709
				if( Raw_Money_Flow > 957332 )
					if( smoothD_d <= 49.6137 )
						if( Positive_Money_Flow_Sum <= 1.64087e+07 )
							ret := -0.236111
						if( Positive_Money_Flow_Sum > 1.64087e+07 )
							ret := -0.046098
					if( smoothD_d > 49.6137 )
						if( MFI <= 2.21529 )
							ret := 0.611111
						if( MFI > 2.21529 )
							ret := -0.004854
		if( Positive_Money_Flow > 3465.65 )
			if( Negative_Money_Flow_Sum <= 1.86779e+08 )
				if( Negative_Money_Flow_Sum <= 1.1771e+08 )
					if( Positive_Money_Flow <= 3.22828e+06 )
						if( rsi1 <= 41.3972 )
							ret := 0.033884
						if( rsi1 > 41.3972 )
							ret := -0.204599
					if( Positive_Money_Flow > 3.22828e+06 )
						if( Negative_Money_Flow_Sum <= 6.3588e+06 )
							ret := 0.132653
						if( Negative_Money_Flow_Sum > 6.3588e+06 )
							ret := -0.046997
				if( Negative_Money_Flow_Sum > 1.1771e+08 )
					if( Raw_Money_Flow <= 5.35928e+07 )
						if( Typical_Price <= 129.9 )
							ret := 0.133041
						if( Typical_Price > 129.9 )
							ret := -0.055402
					if( Raw_Money_Flow > 5.35928e+07 )
						if( k <= 83.8354 )
							ret := 0.510417
						if( k > 83.8354 )
							ret := -0.100000
			if( Negative_Money_Flow_Sum > 1.86779e+08 )
				if( d <= 20.7498 )
					if( Positive_Money_Flow_Sum <= 2.10409e+08 )
						if( Typical_Price <= 148.045 )
							ret := -0.113772
						if( Typical_Price > 148.045 )
							ret := 0.151093
					if( Positive_Money_Flow_Sum > 2.10409e+08 )
						if( Positive_Money_Flow_Sum <= 3.32081e+08 )
							ret := -0.486631
						if( Positive_Money_Flow_Sum > 3.32081e+08 )
							ret := 0.202020
				if( d > 20.7498 )
					if( Money_Flow_Ratio <= 0.377011 )
						if( MFI_Low <= -18.9981 )
							ret := 0.295455
						if( MFI_Low > -18.9981 )
							ret := -0.485549
					if( Money_Flow_Ratio > 0.377011 )
						if( Positive_Money_Flow_Sum <= 3.34675e+08 )
							ret := -0.321696
						if( Positive_Money_Flow_Sum > 3.34675e+08 )
							ret := 0.009843
	if( d_k > -1.16466 )
		if( Raw_Money_Flow <= 707337 )
			if( Negative_Money_Flow <= 30.1532 )
				if( Typical_Price <= 41.445 )
					if( MFI <= 33.7799 )
						if( d <= 97.1315 )
							ret := -0.317241
						if( d > 97.1315 )
							ret := 0.785714 // buy
					if( MFI > 33.7799 )
						if( Money_Flow_Ratio <= 5.78913 )
							ret := 0.231461
						if( Money_Flow_Ratio > 5.78913 )
							ret := 0.672414
				if( Typical_Price > 41.445 )
					if( Negative_Money_Flow_Sum <= 7.29216e+07 )
						if( rsi1 <= 43.813 )
							ret := 0.147260
						if( rsi1 > 43.813 )
							ret := -0.208054
					if( Negative_Money_Flow_Sum > 7.29216e+07 )
						if( Positive_Money_Flow_Sum <= 1.06327e+06 )
							ret := 0.772727 // buy
						if( Positive_Money_Flow_Sum > 1.06327e+06 )
							ret := 0.033429
			if( Negative_Money_Flow > 30.1532 )
				if( MFI_High <= -49.9832 )
					if( d_k <= 0.809558 )
						if( rsi1 <= 63.7117 )
							ret := 0.311966
						if( rsi1 > 63.7117 )
							ret := -1.000000 // sell
					if( d_k > 0.809558 )
						if( MFI_High <= -76.0242 )
							ret := 0.256831
						if( MFI_High > -76.0242 )
							ret := -0.048424
				if( MFI_High > -49.9832 )
					if( Typical_Price <= 58.3237 )
						if( rsi1 <= 38.3394 )
							ret := 0.632391
						if( rsi1 > 38.3394 )
							ret := 0.348971
					if( Typical_Price > 58.3237 )
						if( d_k <= 20.1434 )
							ret := 0.148590
						if( d_k > 20.1434 )
							ret := 0.447368
		if( Raw_Money_Flow > 707337 )
			if( MFI_High <= -79.4281 )
				if( Negative_Money_Flow <= 4.4279e+07 )
					if( Negative_Money_Flow_Sum <= 1.04865e+08 )
						if( Negative_Money_Flow <= 1.20351e+07 )
							ret := 0.355556
						if( Negative_Money_Flow > 1.20351e+07 )
							ret := -0.433333
					if( Negative_Money_Flow_Sum > 1.04865e+08 )
						if( rsi1 <= 33.0949 )
							ret := 0.782123 // buy
						if( rsi1 > 33.0949 )
							ret := 0.243243
				if( Negative_Money_Flow > 4.4279e+07 )
					if( Negative_Money_Flow_Sum <= 2.60198e+08 )
						if( Raw_Money_Flow <= 4.93206e+07 )
							ret := -0.833333 // sell
						if( Raw_Money_Flow > 4.93206e+07 )
							ret := 0.815789 // buy
					if( Negative_Money_Flow_Sum > 2.60198e+08 )
						if( Typical_Price <= 272.577 )
							ret := -0.630769
						if( Typical_Price > 272.577 )
							ret := 0.391304
			if( MFI_High > -79.4281 )
				if( Money_Flow_Ratio <= 48.8586 )
					if( rsi1 <= 65.1281 )
						if( Negative_Money_Flow_Sum <= 8.11623e+08 )
							ret := -0.016268
						if( Negative_Money_Flow_Sum > 8.11623e+08 )
							ret := -0.445887
					if( rsi1 > 65.1281 )
						if( Positive_Money_Flow_Sum <= 5.25746e+07 )
							ret := -0.041212
						if( Positive_Money_Flow_Sum > 5.25746e+07 )
							ret := 0.105277
				if( Money_Flow_Ratio > 48.8586 )
					if( Typical_Price <= 95.82 )
						if( Positive_Money_Flow <= 559652 )
							ret := 1.000000 // buy
						if( Positive_Money_Flow > 559652 )
							ret := -0.100806
					if( Typical_Price > 95.82 )
						if( Raw_Money_Flow <= 1.20681e+08 )
							ret := -0.659420
						if( Raw_Money_Flow > 1.20681e+08 )
							ret := 0.619048
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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


//CODE associated with the technical indicator L_Stochastic_RSI 
//@version=5
//indicator title="Stochastic RSI", shorttitle="Stoch RSI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
smoothK = input.int(3, "K", minval=1)
smoothD = input.int(3, "D", minval=1)
lengthRSI = input.int(14, "RSI Length", minval=1)
lengthStoch = input.int(14, "Stochastic Length", minval=1)
src = input(close, title="RSI Source")
rsi1 = ta.rsi(src, lengthRSI)
k = ta.sma(ta.stoch(rsi1, rsi1, rsi1, lengthStoch), smoothK)
d = ta.sma(k, smoothD)
plot(k, "K", color=#2962FF)
plot(d, "D", color=#FF6D00)

d_k = d - k
smoothD_d = d - smoothD
smoothK_k = k - smoothK

h0 = hline(80, "Upper Band", color=#787B86)
hline(50, "Middle Band", color=color.new(#787B86, 50))
h1 = hline(20, "Lower Band", color=#787B86)
fill(h0, h1, color=color.rgb(33, 150, 243, 90), title="Background")
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
float op_operation = decision_tree_0_TWLO_30Min_6e53b79c(Typical_Price, MFI_High, Negative_Money_Flow, Positive_Money_Flow, Money_Flow_Ratio, MFI, Negative_Money_Flow_Sum, Positive_Money_Flow_Sum, MFI_Low, Raw_Money_Flow, rsi1, d, k, smoothD_d, d_k, smoothK_k)

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



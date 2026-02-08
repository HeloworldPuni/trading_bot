//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Stochastic_RSI
// ID_model: ADSK_1Hour_2MS0_0f6a7b56 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_ADSK_1Hour_2MS0_0f6a7b56", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_ADSK_1Hour_0f6a7b56(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, rsi1, smoothK_k, d_k, k, d, smoothD_d)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( Positive_Money_Flow_Sum <= 1.13367e+08 )
		if( d_k <= 3.76785 )
			if( MFI <= 6.46099 )
				if( Raw_Money_Flow <= 5.71528e+06 )
					if( Raw_Money_Flow <= 49907.1 )
						ret := 0.555556
					if( Raw_Money_Flow > 49907.1 )
						if( d <= 4.21441 )
							ret := 0.818182 // buy
						if( d > 4.21441 )
							ret := 1.000000 // buy
				if( Raw_Money_Flow > 5.71528e+06 )
					if( Raw_Money_Flow <= 6.63243e+07 )
						if( Negative_Money_Flow_Sum <= 5.65958e+08 )
							ret := 0.535714
						if( Negative_Money_Flow_Sum > 5.65958e+08 )
							ret := -0.730769 // sell
					if( Raw_Money_Flow > 6.63243e+07 )
						if( MFI_Low <= -15.7587 )
							ret := 0.913043 // buy
						if( MFI_Low > -15.7587 )
							ret := 0.454545
			if( MFI > 6.46099 )
				if( Typical_Price <= 174.378 )
					if( smoothD_d <= 0.110798 )
						if( d_k <= -0.222277 )
							ret := -0.520000
						if( d_k > -0.222277 )
							ret := 0.045455
					if( smoothD_d > 0.110798 )
						if( d_k <= -11.8295 )
							ret := 0.083333
						if( d_k > -11.8295 )
							ret := 0.709677 // buy
				if( Typical_Price > 174.378 )
					if( Positive_Money_Flow_Sum <= 8.18994e+07 )
						if( Raw_Money_Flow <= 4.09713e+07 )
							ret := -0.077830
						if( Raw_Money_Flow > 4.09713e+07 )
							ret := -0.491018
					if( Positive_Money_Flow_Sum > 8.18994e+07 )
						if( smoothK_k <= 6.39679 )
							ret := -0.173913
						if( smoothK_k > 6.39679 )
							ret := 0.288889
		if( d_k > 3.76785 )
			if( Positive_Money_Flow_Sum <= 5.91995e+07 )
				if( Negative_Money_Flow_Sum <= 4.22725e+08 )
					if( k <= 32.9291 )
						if( Raw_Money_Flow <= 2.3096e+07 )
							ret := -0.880000 // sell
						if( Raw_Money_Flow > 2.3096e+07 )
							ret := -0.200000
					if( k > 32.9291 )
						if( MFI_High <= -57.6696 )
							ret := 0.181818
						if( MFI_High > -57.6696 )
							ret := 1.000000 // buy
				if( Negative_Money_Flow_Sum > 4.22725e+08 )
					if( Positive_Money_Flow_Sum <= 5.58314e+07 )
						if( d_k <= 6.3414 )
							ret := 0.777778 // buy
						if( d_k > 6.3414 )
							ret := 1.000000 // buy
					if( Positive_Money_Flow_Sum > 5.58314e+07 )
						ret := 0.250000
			if( Positive_Money_Flow_Sum > 5.91995e+07 )
				if( Negative_Money_Flow_Sum <= 2.82947e+08 )
					if( Positive_Money_Flow <= 7.20417e+06 )
						if( Typical_Price <= 170.573 )
							ret := 0.849057 // buy
						if( Typical_Price > 170.573 )
							ret := 0.371134
					if( Positive_Money_Flow > 7.20417e+06 )
						if( d_k <= 8.92295 )
							ret := 0.272727
						if( d_k > 8.92295 )
							ret := -0.611111
				if( Negative_Money_Flow_Sum > 2.82947e+08 )
					if( Typical_Price <= 259.774 )
						if( rsi1 <= 43.2185 )
							ret := 0.835052 // buy
						if( rsi1 > 43.2185 )
							ret := 0.300000
					if( Typical_Price > 259.774 )
						if( Negative_Money_Flow <= 2.8532e+07 )
							ret := 0.700000 // buy
						if( Negative_Money_Flow > 2.8532e+07 )
							ret := -0.384615
	if( Positive_Money_Flow_Sum > 1.13367e+08 )
		if( smoothD_d <= 6.441 )
			if( Typical_Price <= 208.074 )
				if( Money_Flow_Ratio <= 0.554032 )
					if( smoothD_d <= -2.05732 )
						if( Raw_Money_Flow <= 1.10063e+08 )
							ret := 0.500000
						if( Raw_Money_Flow > 1.10063e+08 )
							ret := 1.000000 // buy
					if( smoothD_d > -2.05732 )
						if( Negative_Money_Flow <= 2.42132e+07 )
							ret := -0.089552
						if( Negative_Money_Flow > 2.42132e+07 )
							ret := -0.518750
				if( Money_Flow_Ratio > 0.554032 )
					if( Positive_Money_Flow_Sum <= 2.52712e+08 )
						if( Typical_Price <= 186.543 )
							ret := 0.016484
						if( Typical_Price > 186.543 )
							ret := 0.361111
					if( Positive_Money_Flow_Sum > 2.52712e+08 )
						if( Typical_Price <= 207.357 )
							ret := -0.209524
						if( Typical_Price > 207.357 )
							ret := 0.600000
			if( Typical_Price > 208.074 )
				if( Negative_Money_Flow <= 4.45212e+07 )
					if( rsi1 <= 11.431 )
						if( Negative_Money_Flow_Sum <= 5.34709e+08 )
							ret := 0.000000
						if( Negative_Money_Flow_Sum > 5.34709e+08 )
							ret := 0.875000 // buy
					if( rsi1 > 11.431 )
						if( rsi1 <= 39.5959 )
							ret := -0.437023
						if( rsi1 > 39.5959 )
							ret := -0.270588
				if( Negative_Money_Flow > 4.45212e+07 )
					if( Positive_Money_Flow_Sum <= 1.46217e+08 )
						if( Raw_Money_Flow <= 6.35575e+07 )
							ret := -0.100000
						if( Raw_Money_Flow > 6.35575e+07 )
							ret := -0.785714 // sell
					if( Positive_Money_Flow_Sum > 1.46217e+08 )
						if( smoothK_k <= 5.1836 )
							ret := 0.407895
						if( smoothK_k > 5.1836 )
							ret := -0.454545
		if( smoothD_d > 6.441 )
			if( Typical_Price <= 145.352 )
				if( Negative_Money_Flow_Sum <= 1.69589e+08 )
					if( Negative_Money_Flow_Sum <= 9.17601e+07 )
						if( d_k <= -2.02592 )
							ret := -0.805556 // sell
						if( d_k > -2.02592 )
							ret := -0.047619
					if( Negative_Money_Flow_Sum > 9.17601e+07 )
						if( Negative_Money_Flow_Sum <= 1.27836e+08 )
							ret := 0.445946
						if( Negative_Money_Flow_Sum > 1.27836e+08 )
							ret := -0.191083
				if( Negative_Money_Flow_Sum > 1.69589e+08 )
					if( MFI <= 64.386 )
						if( Negative_Money_Flow_Sum <= 4.87459e+08 )
							ret := 0.235789
						if( Negative_Money_Flow_Sum > 4.87459e+08 )
							ret := 0.800000 // buy
					if( MFI > 64.386 )
						if( rsi1 <= 66.1548 )
							ret := 1.000000 // buy
						if( rsi1 > 66.1548 )
							ret := 0.307692
			if( Typical_Price > 145.352 )
				if( Negative_Money_Flow_Sum <= 1.09143e+08 )
					if( Typical_Price <= 190.837 )
						if( Positive_Money_Flow_Sum <= 4.13185e+08 )
							ret := 0.299363
						if( Positive_Money_Flow_Sum > 4.13185e+08 )
							ret := -0.066667
					if( Typical_Price > 190.837 )
						if( Positive_Money_Flow_Sum <= 2.23019e+08 )
							ret := -0.195402
						if( Positive_Money_Flow_Sum > 2.23019e+08 )
							ret := 0.090620
				if( Negative_Money_Flow_Sum > 1.09143e+08 )
					if( Negative_Money_Flow_Sum <= 2.20679e+08 )
						if( d <= 76.453 )
							ret := -0.058229
						if( d > 76.453 )
							ret := -0.196225
					if( Negative_Money_Flow_Sum > 2.20679e+08 )
						if( Negative_Money_Flow <= 1.0647e+08 )
							ret := -0.001069
						if( Negative_Money_Flow > 1.0647e+08 )
							ret := 0.286783
	
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
float op_operation = decision_tree_0_ADSK_1Hour_0f6a7b56(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, rsi1, smoothK_k, d_k, k, d, smoothD_d)

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



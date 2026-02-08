//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Triple_EMA
// ID_model: TWLO_5Min_2MT0_de5f3ec7 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_TWLO_5Min_2MT0_de5f3ec7", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_TWLO_5Min_de5f3ec7(Typical_Price, MFI_High, Negative_Money_Flow, Positive_Money_Flow, Money_Flow_Ratio, MFI, Negative_Money_Flow_Sum, Positive_Money_Flow_Sum, MFI_Low, Raw_Money_Flow, ema2, ema1, ema12, ema3, ema13, tema)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( Negative_Money_Flow <= 386.535 )
		if( Raw_Money_Flow <= 398654 )
			if( ema12 <= 0.188349 )
				if( Positive_Money_Flow <= 1392.8 )
					if( ema13 <= -0.170795 )
						if( ema3 <= 59.8695 )
							ret := -0.307692
						if( ema3 > 59.8695 )
							ret := -0.708333 // sell
					if( ema13 > -0.170795 )
						if( Negative_Money_Flow_Sum <= 109092 )
							ret := 0.666667
						if( Negative_Money_Flow_Sum > 109092 )
							ret := 0.140496
				if( Positive_Money_Flow > 1392.8 )
					if( MFI_High <= -64.2868 )
						if( ema12 <= 0.006391 )
							ret := 0.194842
						if( ema12 > 0.006391 )
							ret := -0.269841
					if( MFI_High > -64.2868 )
						if( Positive_Money_Flow_Sum <= 102968 )
							ret := 0.342857
						if( Positive_Money_Flow_Sum > 102968 )
							ret := -0.190896
			if( ema12 > 0.188349 )
				if( ema3 <= 59.4691 )
					if( Negative_Money_Flow_Sum <= 187395 )
						if( Negative_Money_Flow_Sum <= 134471 )
							ret := -0.058824
						if( Negative_Money_Flow_Sum > 134471 )
							ret := 0.840000 // buy
					if( Negative_Money_Flow_Sum > 187395 )
						if( ema13 <= 0.507934 )
							ret := -0.372093
						if( ema13 > 0.507934 )
							ret := 0.263158
				if( ema3 > 59.4691 )
					if( Negative_Money_Flow_Sum <= 502245 )
						if( MFI <= 77.993 )
							ret := -0.141026
						if( MFI > 77.993 )
							ret := -0.642857
					if( Negative_Money_Flow_Sum > 502245 )
						if( ema13 <= 0.493151 )
							ret := -0.674074
						if( ema13 > 0.493151 )
							ret := -0.984848 // sell
		if( Raw_Money_Flow > 398654 )
			if( ema13 <= -0.463238 )
				if( Positive_Money_Flow_Sum <= 3.9018e+07 )
					if( MFI <= 17.9957 )
						if( ema12 <= -0.300782 )
							ret := -0.846154 // sell
						if( ema12 > -0.300782 )
							ret := 0.166667
					if( MFI > 17.9957 )
						if( Raw_Money_Flow <= 3.87104e+06 )
							ret := -0.259786
						if( Raw_Money_Flow > 3.87104e+06 )
							ret := 0.115942
				if( Positive_Money_Flow_Sum > 3.9018e+07 )
					if( ema3 <= 65.8149 )
						if( ema3 <= 63.0673 )
							ret := -0.765957 // sell
						if( ema3 > 63.0673 )
							ret := -0.230769
					if( ema3 > 65.8149 )
						if( ema1 <= 67.5482 )
							ret := -1.000000 // sell
						if( ema1 > 67.5482 )
							ret := -0.777778 // sell
			if( ema13 > -0.463238 )
				if( MFI <= 93.8668 )
					if( Positive_Money_Flow <= 1.72562e+07 )
						if( ema12 <= 0.146288 )
							ret := -0.026464
						if( ema12 > 0.146288 )
							ret := -0.151914
					if( Positive_Money_Flow > 1.72562e+07 )
						if( Negative_Money_Flow_Sum <= 7.83462e+06 )
							ret := 0.928571 // buy
						if( Negative_Money_Flow_Sum > 7.83462e+06 )
							ret := -0.688742
				if( MFI > 93.8668 )
					if( Money_Flow_Ratio <= 68.5567 )
						if( Negative_Money_Flow_Sum <= 134423 )
							ret := 0.872340 // buy
						if( Negative_Money_Flow_Sum > 134423 )
							ret := 0.214286
					if( Money_Flow_Ratio > 68.5567 )
						if( ema2 <= 58.9149 )
							ret := 0.303797
						if( ema2 > 58.9149 )
							ret := -0.354331
	if( Negative_Money_Flow > 386.535 )
		if( Negative_Money_Flow <= 126911 )
			if( ema12 <= 0.032706 )
				if( Positive_Money_Flow_Sum <= 1.1806e+07 )
					if( Typical_Price <= 62.318 )
						if( Negative_Money_Flow_Sum <= 228546 )
							ret := 0.614973
						if( Negative_Money_Flow_Sum > 228546 )
							ret := 0.265403
					if( Typical_Price > 62.318 )
						if( Money_Flow_Ratio <= 1.2092 )
							ret := 0.201178
						if( Money_Flow_Ratio > 1.2092 )
							ret := -0.177570
				if( Positive_Money_Flow_Sum > 1.1806e+07 )
					if( Negative_Money_Flow_Sum <= 5.04335e+06 )
						if( ema12 <= -0.023433 )
							ret := 0.408696
						if( ema12 > -0.023433 )
							ret := -0.228571
					if( Negative_Money_Flow_Sum > 5.04335e+06 )
						if( MFI_Low <= 59.4869 )
							ret := 0.515517
						if( MFI_Low > 59.4869 )
							ret := 0.860140 // buy
			if( ema12 > 0.032706 )
				if( Negative_Money_Flow_Sum <= 2.07771e+07 )
					if( MFI_Low <= 38.3734 )
						if( Negative_Money_Flow_Sum <= 909241 )
							ret := -0.111628
						if( Negative_Money_Flow_Sum > 909241 )
							ret := -0.614887
					if( MFI_Low > 38.3734 )
						if( ema13 <= 0.509932 )
							ret := 0.183639
						if( ema13 > 0.509932 )
							ret := -0.744681 // sell
				if( Negative_Money_Flow_Sum > 2.07771e+07 )
					if( MFI <= 64.1893 )
						if( Raw_Money_Flow <= 195214 )
							ret := 0.373057
						if( Raw_Money_Flow > 195214 )
							ret := 0.953488 // buy
					if( MFI > 64.1893 )
						ret := -0.350000
		if( Negative_Money_Flow > 126911 )
			if( Negative_Money_Flow <= 1.71986e+06 )
				if( Negative_Money_Flow_Sum <= 1.49512e+07 )
					if( ema1 <= 56.3525 )
						if( MFI_Low <= 65.6247 )
							ret := 0.040958
						if( MFI_Low > 65.6247 )
							ret := 0.923077 // buy
					if( ema1 > 56.3525 )
						if( Positive_Money_Flow_Sum <= 188489 )
							ret := 0.312977
						if( Positive_Money_Flow_Sum > 188489 )
							ret := -0.075709
				if( Negative_Money_Flow_Sum > 1.49512e+07 )
					if( ema13 <= -0.364346 )
						if( Negative_Money_Flow <= 563548 )
							ret := 0.703704 // buy
						if( Negative_Money_Flow > 563548 )
							ret := -0.435484
					if( ema13 > -0.364346 )
						if( Money_Flow_Ratio <= 1.47336 )
							ret := 0.216578
						if( Money_Flow_Ratio > 1.47336 )
							ret := -0.308725
			if( Negative_Money_Flow > 1.71986e+06 )
				if( Money_Flow_Ratio <= 0.914231 )
					if( MFI_High <= -68.1193 )
						if( Negative_Money_Flow_Sum <= 2.06801e+07 )
							ret := 0.072978
						if( Negative_Money_Flow_Sum > 2.06801e+07 )
							ret := -0.429799
					if( MFI_High > -68.1193 )
						if( tema <= 52.5318 )
							ret := 0.564912
						if( tema > 52.5318 )
							ret := 0.157758
				if( Money_Flow_Ratio > 0.914231 )
					if( Positive_Money_Flow_Sum <= 3.83341e+07 )
						if( Raw_Money_Flow <= 3.33357e+06 )
							ret := -0.026087
						if( Raw_Money_Flow > 3.33357e+06 )
							ret := -0.248109
					if( Positive_Money_Flow_Sum > 3.83341e+07 )
						if( Positive_Money_Flow_Sum <= 1.75859e+08 )
							ret := 0.237624
						if( Positive_Money_Flow_Sum > 1.75859e+08 )
							ret := -0.951220 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
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


//CODE associated with the technical indicator L_Triple_EMA 
//@version=5
//indicator title="Triple EMA", shorttitle="TEMA", overlay=true, timeframe="", timeframe_gaps=true)
length_TEMA = input.int(9, minval=1)
ema1 = ta.ema(close, length_TEMA)
ema2 = ta.ema(ema1, length_TEMA)
ema3 = ta.ema(ema2, length_TEMA)
tema = 3 * (ema1 - ema2) + ema3
plot(tema, "TEMA", color=#2962FF)

ema12 = ema1 - ema2
ema13 = ema1 - ema3


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
float op_operation = decision_tree_0_TWLO_5Min_de5f3ec7(Typical_Price, MFI_High, Negative_Money_Flow, Positive_Money_Flow, Money_Flow_Ratio, MFI, Negative_Money_Flow_Sum, Positive_Money_Flow_Sum, MFI_Low, Raw_Money_Flow, ema2, ema1, ema12, ema3, ema13, tema)

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



//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Vortex_Indicator
// ID_model: AFRM_1Hour_2MV0_08aa031d Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AFRM_1Hour_2MV0_08aa031d", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AFRM_1Hour_08aa031d(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, VIP, VIM, VIP_VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( VIP_VIM <= 0.471473 )
		if( Negative_Money_Flow_Sum <= 1.54594e+08 )
			if( Typical_Price <= 69.1664 )
				if( Positive_Money_Flow_Sum <= 7.75355e+07 )
					if( Raw_Money_Flow <= 1.76915e+07 )
						if( VIP <= 0.922328 )
							ret := -0.110454
						if( VIP > 0.922328 )
							ret := 0.131264
					if( Raw_Money_Flow > 1.76915e+07 )
						if( Typical_Price <= 11.8545 )
							ret := -0.042373
						if( Typical_Price > 11.8545 )
							ret := 0.332651
				if( Positive_Money_Flow_Sum > 7.75355e+07 )
					if( Money_Flow_Ratio <= 0.787851 )
						if( VIM <= 1.1062 )
							ret := -0.539568
						if( VIM > 1.1062 )
							ret := -0.096154
					if( Money_Flow_Ratio > 0.787851 )
						if( Negative_Money_Flow_Sum <= 1.47831e+08 )
							ret := 0.002313
						if( Negative_Money_Flow_Sum > 1.47831e+08 )
							ret := 0.421384
			if( Typical_Price > 69.1664 )
				if( MFI_High <= -13.2232 )
					if( Positive_Money_Flow <= 21065.5 )
						if( VIP <= 0.8085 )
							ret := -0.793103 // sell
						if( VIP > 0.8085 )
							ret := -0.151220
					if( Positive_Money_Flow > 21065.5 )
						if( Raw_Money_Flow <= 2.15137e+06 )
							ret := -0.695238
						if( Raw_Money_Flow > 2.15137e+06 )
							ret := -0.369748
				if( MFI_High > -13.2232 )
					if( Positive_Money_Flow <= 3.1446e+07 )
						if( Negative_Money_Flow_Sum <= 1.2327e+08 )
							ret := 0.369748
						if( Negative_Money_Flow_Sum > 1.2327e+08 )
							ret := -0.677419
					if( Positive_Money_Flow > 3.1446e+07 )
						if( Raw_Money_Flow <= 1.33937e+08 )
							ret := -0.645833
						if( Raw_Money_Flow > 1.33937e+08 )
							ret := 0.222222
		if( Negative_Money_Flow_Sum > 1.54594e+08 )
			if( MFI_Low <= -16.6195 )
				if( VIP <= 0.536385 )
					if( Positive_Money_Flow_Sum <= 987615 )
						ret := 0.000000
					if( Positive_Money_Flow_Sum > 987615 )
						if( VIM <= 1.52601 )
							ret := -1.000000 // sell
						if( VIM > 1.52601 )
							ret := -0.600000
				if( VIP > 0.536385 )
					if( VIP_VIM <= -0.659002 )
						if( VIP <= 0.602321 )
							ret := 0.272727
						if( VIP > 0.602321 )
							ret := 0.792079 // buy
					if( VIP_VIM > -0.659002 )
						if( Negative_Money_Flow <= 412008 )
							ret := 0.729167 // buy
						if( Negative_Money_Flow > 412008 )
							ret := 0.104167
			if( MFI_Low > -16.6195 )
				if( Raw_Money_Flow <= 532646 )
					if( Money_Flow_Ratio <= 1.93426 )
						if( MFI_Low <= 31.2321 )
							ret := -0.221500
						if( MFI_Low > 31.2321 )
							ret := -0.529781
					if( Money_Flow_Ratio > 1.93426 )
						if( Negative_Money_Flow_Sum <= 1.28431e+09 )
							ret := 0.261261
						if( Negative_Money_Flow_Sum > 1.28431e+09 )
							ret := -1.000000 // sell
				if( Raw_Money_Flow > 532646 )
					if( Negative_Money_Flow_Sum <= 3.41698e+09 )
						if( Raw_Money_Flow <= 3.15413e+08 )
							ret := -0.039740
						if( Raw_Money_Flow > 3.15413e+08 )
							ret := -0.518519
					if( Negative_Money_Flow_Sum > 3.41698e+09 )
						if( Typical_Price <= 102.436 )
							ret := -1.000000 // sell
						if( Typical_Price > 102.436 )
							ret := -0.333333
	if( VIP_VIM > 0.471473 )
		if( Raw_Money_Flow <= 5.80784e+07 )
			if( Positive_Money_Flow <= 439200 )
				if( MFI_Low <= 28.488 )
					if( Raw_Money_Flow <= 57941.6 )
						ret := 1.000000 // buy
					if( Raw_Money_Flow > 57941.6 )
						ret := 0.888889 // buy
				if( MFI_Low > 28.488 )
					if( Typical_Price <= 48.9131 )
						if( VIM <= 0.860676 )
							ret := 0.242953
						if( VIM > 0.860676 )
							ret := -0.615385
					if( Typical_Price > 48.9131 )
						if( Positive_Money_Flow_Sum <= 1.40186e+08 )
							ret := -0.457831
						if( Positive_Money_Flow_Sum > 1.40186e+08 )
							ret := 0.084577
			if( Positive_Money_Flow > 439200 )
				if( MFI <= 83.1538 )
					if( Positive_Money_Flow_Sum <= 1.55735e+08 )
						if( Positive_Money_Flow_Sum <= 1.43537e+08 )
							ret := 0.401460
						if( Positive_Money_Flow_Sum > 1.43537e+08 )
							ret := -0.684211
					if( Positive_Money_Flow_Sum > 1.55735e+08 )
						if( VIP <= 1.39224 )
							ret := 0.745833 // buy
						if( VIP > 1.39224 )
							ret := 0.326087
				if( MFI > 83.1538 )
					if( Typical_Price <= 107.565 )
						if( VIM <= 0.767 )
							ret := 0.351421
						if( VIM > 0.767 )
							ret := -0.210526
					if( Typical_Price > 107.565 )
						ret := -0.727273 // sell
		if( Raw_Money_Flow > 5.80784e+07 )
			if( Money_Flow_Ratio <= 122.904 )
				if( Negative_Money_Flow_Sum <= 1.83625e+07 )
					if( Positive_Money_Flow_Sum <= 5.04166e+08 )
						if( VIM <= 0.616257 )
							ret := 0.454545
						if( VIM > 0.616257 )
							ret := 1.000000 // buy
					if( Positive_Money_Flow_Sum > 5.04166e+08 )
						ret := 0.000000
				if( Negative_Money_Flow_Sum > 1.83625e+07 )
					if( Raw_Money_Flow <= 6.8768e+07 )
						if( Positive_Money_Flow_Sum <= 3.2904e+08 )
							ret := -0.740000 // sell
						if( Positive_Money_Flow_Sum > 3.2904e+08 )
							ret := 0.000000
					if( Raw_Money_Flow > 6.8768e+07 )
						if( Typical_Price <= 49.7661 )
							ret := -0.074866
						if( Typical_Price > 49.7661 )
							ret := 0.283465
			if( Money_Flow_Ratio > 122.904 )
				if( Money_Flow_Ratio <= 1246.05 )
					if( Positive_Money_Flow_Sum <= 4.85191e+08 )
						if( Typical_Price <= 19.741 )
							ret := -0.916667 // sell
						if( Typical_Price > 19.741 )
							ret := -0.150000
					if( Positive_Money_Flow_Sum > 4.85191e+08 )
						if( VIP <= 1.34684 )
							ret := -1.000000 // sell
						if( VIP > 1.34684 )
							ret := -0.700000 // sell
				if( Money_Flow_Ratio > 1246.05 )
					ret := 0.400000
	
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


//CODE associated with the technical indicator L_Vortex_Indicator 
//@version=5
//indicator title = "Vortex Indicator", shorttitle="VI", format=format.price, precision=4, timeframe="", timeframe_gaps=true)
period_ = input.int(14, title="Length", minval=2)
VMP = math.sum( math.abs( high - low[1]), period_ )
VMM = math.sum( math.abs( low - high[1]), period_ )
STR = math.sum( ta.atr(1), period_ )
VIP = VMP / STR
VIM = VMM / STR

VIP_VIM = VIP - VIM

plot(VIP, title="VI +", color=#2962FF)
plot(VIM, title="VI -", color=#E91E63)
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
float op_operation = decision_tree_0_AFRM_1Hour_08aa031d(Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum, VIP, VIM, VIP_VIM)

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



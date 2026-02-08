//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Chaikin_Money_Flow, L_Money_Flow_Index
// ID_model: TTD_1Day_2CM0_03fc5311 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_TTD_1Day_2CM0_03fc5311", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_TTD_1Day_03fc5311(ad_mf, mf, ad, Typical_Price, MFI_High, Negative_Money_Flow, Positive_Money_Flow, Money_Flow_Ratio, MFI, Negative_Money_Flow_Sum, Positive_Money_Flow_Sum, MFI_Low, Raw_Money_Flow)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=5, max_features=0.6, max_leaf_nodes=30,min_samples_split=5, random_state=843828734)
	if( Positive_Money_Flow_Sum <= 2.68982e+08 )
		if( Typical_Price <= 29.6997 )
			if( MFI_High <= -31.7167 )
				if( ad_mf <= 155647 )
					if( mf <= 0.024761 )
						ret := 0.916667 // buy
					if( mf > 0.024761 )
						ret := 0.000000
				if( ad_mf > 155647 )
					ret := 0.000000
			if( MFI_High > -31.7167 )
				if( mf <= -0.212919 )
					if( Negative_Money_Flow_Sum <= 5.81378e+07 )
						ret := -0.500000
					if( Negative_Money_Flow_Sum > 5.81378e+07 )
						ret := 1.000000 // buy
				if( mf > -0.212919 )
					if( Negative_Money_Flow <= 8.16198e+06 )
						ret := -0.864865 // sell
					if( Negative_Money_Flow > 8.16198e+06 )
						ret := 0.000000
		if( Typical_Price > 29.6997 )
			if( Money_Flow_Ratio <= 0.423037 )
				if( Negative_Money_Flow_Sum <= 1.24609e+09 )
					if( Money_Flow_Ratio <= 0.211715 )
						ret := 0.500000
					if( Money_Flow_Ratio > 0.211715 )
						ret := 0.000000
				if( Negative_Money_Flow_Sum > 1.24609e+09 )
					ret := -1.000000 // sell
			if( Money_Flow_Ratio > 0.423037 )
				if( Positive_Money_Flow <= 661079 )
					if( mf <= 0.009731 )
						ret := 0.333333
					if( mf > 0.009731 )
						ret := 1.000000 // buy
				if( Positive_Money_Flow > 661079 )
					if( Typical_Price <= 38.4093 )
						ret := 0.785714 // buy
					if( Typical_Price > 38.4093 )
						ret := 1.000000 // buy
	if( Positive_Money_Flow_Sum > 2.68982e+08 )
		if( MFI <= 31.9978 )
			if( mf <= -0.013155 )
				if( Typical_Price <= 68.0091 )
					if( ad_mf <= 6.29228e+06 )
						ret := 0.866667 // buy
					if( ad_mf > 6.29228e+06 )
						ret := 0.000000
				if( Typical_Price > 68.0091 )
					if( Negative_Money_Flow_Sum <= 4.87489e+09 )
						ret := 0.368852
					if( Negative_Money_Flow_Sum > 4.87489e+09 )
						ret := 0.806452 // buy
			if( mf > -0.013155 )
				if( MFI_High <= -49.4625 )
					if( Typical_Price <= 83.4117 )
						ret := -1.000000 // sell
					if( Typical_Price > 83.4117 )
						ret := 0.666667
				if( MFI_High > -49.4625 )
					if( Money_Flow_Ratio <= 0.444071 )
						ret := 0.400000
					if( Money_Flow_Ratio > 0.444071 )
						ret := 0.950000 // buy
		if( MFI > 31.9978 )
			if( Raw_Money_Flow <= 4.65535e+07 )
				if( Positive_Money_Flow_Sum <= 3.95494e+08 )
					if( ad <= -186130 )
						ret := -0.111111
					if( ad > -186130 )
						ret := -0.787500 // sell
				if( Positive_Money_Flow_Sum > 3.95494e+08 )
					if( Positive_Money_Flow_Sum <= 6.75719e+08 )
						ret := -0.025000
					if( Positive_Money_Flow_Sum > 6.75719e+08 )
						ret := -0.700000 // sell
			if( Raw_Money_Flow > 4.65535e+07 )
				if( Positive_Money_Flow_Sum <= 4.27801e+09 )
					if( Positive_Money_Flow <= 4.33157e+08 )
						ret := -0.056180
					if( Positive_Money_Flow > 4.33157e+08 )
						ret := 0.429577
				if( Positive_Money_Flow_Sum > 4.27801e+09 )
					if( mf <= 0.062386 )
						ret := 0.180451
					if( mf > 0.062386 )
						ret := -0.401617
	
    ret //return
// Define expected timeframe based on the selected interval: 1Day pine_value: D   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1DAY !!"
if (str.tostring(timeframe.period) != "D")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Chaikin_Money_Flow 
 //@version=5
//indicator title="Chaikin Money Flow", shorttitle="CMF", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
var cumVol = 0.
cumVol += nz(volume)
if barstate.islast and cumVol == 0
    runtime.error("No volume is provided by the data vendor.")
length_CMF = input.int(20, minval=1)
ad = close==high and close==low or high==low ? 0 : ((2*close-low-high)/(high-low))*volume
mf = math.sum(ad, length_CMF) / math.sum(volume, length_CMF)
plot(mf, color=#43A047, title="MF")
hline(0, color=#787B86, title="Zero", linestyle=hline.style_dashed)


ad_mf = ad - mf

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
float op_operation = decision_tree_0_TTD_1Day_03fc5311(ad_mf, mf, ad, Typical_Price, MFI_High, Negative_Money_Flow, Positive_Money_Flow, Money_Flow_Ratio, MFI, Negative_Money_Flow_Sum, Positive_Money_Flow_Sum, MFI_Low, Raw_Money_Flow)

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



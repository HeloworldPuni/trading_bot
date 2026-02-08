//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Chaikin_Money_Flow, L_Money_Flow_Index
// ID_model: APPS_1Hour_2CM0_53c79a2e Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_APPS_1Hour_2CM0_53c79a2e", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_APPS_1Hour_53c79a2e(ad, mf, ad_mf, Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( ad <= 0.270677 )
		if( Negative_Money_Flow_Sum <= 2.50651e+06 )
			if( Negative_Money_Flow <= 19.2323 )
				if( Raw_Money_Flow <= 4085.91 )
					if( MFI_Low <= -0.652857 )
						ret := 0.875000 // buy
					if( MFI_Low > -0.652857 )
						if( Typical_Price <= 4.34025 )
							ret := -0.363158
						if( Typical_Price > 4.34025 )
							ret := 0.437500
				if( Raw_Money_Flow > 4085.91 )
					if( mf <= 0.005995 )
						if( Positive_Money_Flow_Sum <= 2.32739e+06 )
							ret := 0.594937
						if( Positive_Money_Flow_Sum > 2.32739e+06 )
							ret := -0.207547
					if( mf > 0.005995 )
						if( Positive_Money_Flow_Sum <= 1.18835e+07 )
							ret := -0.033333
						if( Positive_Money_Flow_Sum > 1.18835e+07 )
							ret := 0.467532
			if( Negative_Money_Flow > 19.2323 )
				if( ad_mf <= -116990 )
					if( mf <= -0.183389 )
						if( Negative_Money_Flow_Sum <= 2.16663e+06 )
							ret := 0.730769 // buy
						if( Negative_Money_Flow_Sum > 2.16663e+06 )
							ret := -0.111111
					if( mf > -0.183389 )
						if( ad_mf <= -260152 )
							ret := -0.700000 // sell
						if( ad_mf > -260152 )
							ret := -0.162162
				if( ad_mf > -116990 )
					if( Positive_Money_Flow_Sum <= 1.80949e+06 )
						if( Negative_Money_Flow_Sum <= 1.05822e+06 )
							ret := 0.457576
						if( Negative_Money_Flow_Sum > 1.05822e+06 )
							ret := 0.706349 // buy
					if( Positive_Money_Flow_Sum > 1.80949e+06 )
						if( MFI_High <= -16.5095 )
							ret := -0.005587
						if( MFI_High > -16.5095 )
							ret := 0.496420
		if( Negative_Money_Flow_Sum > 2.50651e+06 )
			if( Money_Flow_Ratio <= 0.365021 )
				if( ad <= -14184.5 )
					if( Typical_Price <= 74.1729 )
						if( Positive_Money_Flow_Sum <= 383266 )
							ret := -0.426471
						if( Positive_Money_Flow_Sum > 383266 )
							ret := 0.081906
					if( Typical_Price > 74.1729 )
						if( mf <= 0.027581 )
							ret := -0.601942
						if( mf > 0.027581 )
							ret := 0.250000
				if( ad > -14184.5 )
					if( mf <= -0.51487 )
						if( MFI_High <= -59.8583 )
							ret := 0.837838 // buy
						if( MFI_High > -59.8583 )
							ret := -0.125000
					if( mf > -0.51487 )
						if( Positive_Money_Flow_Sum <= 1.02214e+07 )
							ret := -0.368485
						if( Positive_Money_Flow_Sum > 1.02214e+07 )
							ret := -0.094571
			if( Money_Flow_Ratio > 0.365021 )
				if( Positive_Money_Flow_Sum <= 3.20722e+08 )
					if( Negative_Money_Flow <= 92.3277 )
						if( MFI_High <= 14.5407 )
							ret := -0.030384
						if( MFI_High > 14.5407 )
							ret := 0.913043 // buy
					if( Negative_Money_Flow > 92.3277 )
						if( Negative_Money_Flow <= 393236 )
							ret := 0.179197
						if( Negative_Money_Flow > 393236 )
							ret := 0.032284
				if( Positive_Money_Flow_Sum > 3.20722e+08 )
					if( Money_Flow_Ratio <= 5.84952 )
						if( Raw_Money_Flow <= 4861 )
							ret := -1.000000 // sell
						if( Raw_Money_Flow > 4861 )
							ret := 0.822581 // buy
					if( Money_Flow_Ratio > 5.84952 )
						if( MFI_High <= 5.19029 )
							ret := -1.000000 // sell
						if( MFI_High > 5.19029 )
							ret := 0.000000
	if( ad > 0.270677 )
		if( ad <= 18728.1 )
			if( Positive_Money_Flow_Sum <= 2.74496e+07 )
				if( Negative_Money_Flow_Sum <= 1.53645e+06 )
					if( Money_Flow_Ratio <= 4.31363 )
						if( MFI_High <= -26.9117 )
							ret := 0.222222
						if( MFI_High > -26.9117 )
							ret := -0.480226
					if( Money_Flow_Ratio > 4.31363 )
						if( Money_Flow_Ratio <= 436.096 )
							ret := 0.645390
						if( Money_Flow_Ratio > 436.096 )
							ret := -0.875000 // sell
				if( Negative_Money_Flow_Sum > 1.53645e+06 )
					if( Positive_Money_Flow <= 1.0791 )
						if( Negative_Money_Flow_Sum <= 4.43906e+06 )
							ret := 0.237762
						if( Negative_Money_Flow_Sum > 4.43906e+06 )
							ret := -0.212521
					if( Positive_Money_Flow > 1.0791 )
						if( Positive_Money_Flow <= 2857.71 )
							ret := -0.692722
						if( Positive_Money_Flow > 2857.71 )
							ret := -0.307588
			if( Positive_Money_Flow_Sum > 2.74496e+07 )
				if( MFI_High <= -12.278 )
					if( Typical_Price <= 19.2164 )
						if( MFI_Low <= 46.9885 )
							ret := 0.716667 // buy
						if( MFI_Low > 46.9885 )
							ret := -0.333333
					if( Typical_Price > 19.2164 )
						if( Negative_Money_Flow_Sum <= 5.18529e+07 )
							ret := -0.215859
						if( Negative_Money_Flow_Sum > 5.18529e+07 )
							ret := 0.066554
				if( MFI_High > -12.278 )
					if( Negative_Money_Flow_Sum <= 5.81593e+07 )
						if( Raw_Money_Flow <= 223174 )
							ret := -0.218263
						if( Raw_Money_Flow > 223174 )
							ret := 0.229167
					if( Negative_Money_Flow_Sum > 5.81593e+07 )
						if( MFI_Low <= 58.4998 )
							ret := -0.636364
						if( MFI_Low > 58.4998 )
							ret := 0.266667
		if( ad > 18728.1 )
			if( Money_Flow_Ratio <= 101.543 )
				if( MFI <= 6.18409 )
					if( Typical_Price <= 2.50085 )
						ret := 1.000000 // buy
					if( Typical_Price > 2.50085 )
						if( ad_mf <= 47774.2 )
							ret := -0.187500
						if( ad_mf > 47774.2 )
							ret := -0.656716
				if( MFI > 6.18409 )
					if( Positive_Money_Flow_Sum <= 1.66385e+06 )
						if( Positive_Money_Flow <= 153605 )
							ret := 0.037415
						if( Positive_Money_Flow > 153605 )
							ret := 0.405000
					if( Positive_Money_Flow_Sum > 1.66385e+06 )
						if( Typical_Price <= 2.46834 )
							ret := -0.250909
						if( Typical_Price > 2.46834 )
							ret := -0.008156
			if( Money_Flow_Ratio > 101.543 )
				if( mf <= 0.300703 )
					if( Negative_Money_Flow_Sum <= 3.82759e+06 )
						if( Money_Flow_Ratio <= 2832.21 )
							ret := -0.966667 // sell
						if( Money_Flow_Ratio > 2832.21 )
							ret := 0.000000
					if( Negative_Money_Flow_Sum > 3.82759e+06 )
						ret := 1.000000 // buy
				if( mf > 0.300703 )
					if( ad <= 581129 )
						if( ad_mf <= 104912 )
							ret := 1.000000 // buy
						if( ad_mf > 104912 )
							ret := -0.058824
					if( ad > 581129 )
						ret := -0.800000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
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
float op_operation = decision_tree_0_APPS_1Hour_53c79a2e(ad, mf, ad_mf, Negative_Money_Flow, MFI_Low, Money_Flow_Ratio, MFI, Raw_Money_Flow, Positive_Money_Flow, Typical_Price, Positive_Money_Flow_Sum, MFI_High, Negative_Money_Flow_Sum)

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



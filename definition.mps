Workflow: assignment

Input:
stringToProcess: String = JSON(stringToProcess)
  pattern: String = JSON(pattern)
  batchSize: Number = JSON(batchSize)
  thresholdSize: Number = JSON(thresholdSize)

Body:
Split():
  forEachProcess = forEach:
  Assemble():
type: Split                                                                     Input:                                                                       type: Assemble
Input:                                                                          iterator = Split.stringToProcess                                             Input:
originalStr = assignment.stringToProcess
  batchSize = assignment.batchSize    Body:                                                                        processedString = forEachProcess.processedString
  count = forEachProcess.count
Output:                                                                         Process():                                                                   Output:
stringToProcess: Array                                                          type: Process                                                                encodedString: String
patter: String                                                                  Input:                                                                       count: Number
                                                                                stringToProcess = forEachProcess.iterator
  pattern = assignment.pattern
                                                                                Output:
                                                                                processedString: String
                                                                                count: Number

                                                                                Output:
                                                                                processedString = Process.processedString
                                                                                count = Process.count


Output:
encodedString = Assemble.encodedString
result = Assemble.count
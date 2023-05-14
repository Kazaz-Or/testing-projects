import type { Config } from '@jest/types'

const baseDir = '<rootDir>/src/app/pass_checker'
const baseTestDir = '<rootDir>/src/tests'

const config: Config.InitialOptions = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  verbose: true,
  collectCoverage: true,
  collectCoverageFrom: [
    `${baseDir}/**/*.ts`
  ]
}

export default config;